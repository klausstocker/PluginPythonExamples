"""Check LeTTo Python exports and optionally run their native-style validators."""

import argparse
import ast
from decimal import Decimal, InvalidOperation
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET


PREFIX = '[PI Plugin1 Python "'
SUFFIX = '"]'

# Each invocation has a fresh import cache, matching a single target evaluation.
WORKER = '''
from contextlib import redirect_stdout
from dataclasses import dataclass
from io import StringIO
import json
import runpy
import sys
from types import ModuleType
import unittest

payload = json.loads(sys.stdin.read())
if payload.get("check_local_defaults"):
    local = runpy.run_path("dataset.py")
    for variable in payload["defaults"]:
        entry = local[variable["name"]]
        if entry.value != variable["value"] or entry.unit != "":
            raise ValueError("Local dataset default/unit differs: " + variable["name"])

@dataclass(frozen=True)
class DatasetVariable:
    name: str
    value: object
    unit: str = ""

class RedirectedStdout:
    def __enter__(self):
        self.output = StringIO()
        self.redirect = redirect_stdout(self.output)
        self.redirect.__enter__()
        return self

    def __exit__(self, *args):
        return self.redirect.__exit__(*args)

    def __str__(self):
        return self.output.getvalue()

dataset = ModuleType("dataset")
for name, value in payload["values"].items():
    setattr(dataset, name, DatasetVariable(name, value))
helpers = ModuleType("helpers")
helpers.RedirectedStdout = RedirectedStdout
sys.modules["dataset"] = dataset
sys.modules["helpers"] = helpers
namespace = {"__name__": "export_validation"}
exec(compile(payload["validation"], "<validation>", "exec"), namespace)
suite = unittest.defaultTestLoader.loadTestsFromTestCase(namespace["Checker"])
result = unittest.TextTestRunner(stream=sys.stderr).run(suite)
sys.exit(0 if result.testsRun and result.wasSuccessful() else 1)
'''


def require(condition, message):
    if not condition:
        raise ValueError(message)


def number(value):
    require(not isinstance(value, bool), "Boolean dataset value is not numeric")
    try:
        result = Decimal(str(value))
    except InvalidOperation as error:
        raise ValueError(f"Invalid numeric dataset value: {value!r}") from error
    require(result.is_finite(), f"Non-finite dataset value: {value!r}")
    return result


def check_python(source, label):
    require(isinstance(source, str), f"{label} must be a Python string")
    tree = ast.parse(source, filename=label)
    compile(tree, label, "exec")
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            require(node.func.id not in ("input", "SimpleNamespace"),
                    f"{label}: unsupported {node.func.id} call")
    return tree


class QuestionText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def check_question(question):
    """Return decoded config and numeric rows, or raise a descriptive error."""
    require(question.get("type") == "MoodleClozeCalc", "Expected MoodleClozeCalc")
    require(question.findtext("questionType") == "22", "Expected questionType 22")
    require(bool(question.findtext("name")), "Question name is missing")
    for field in ("sendToParser", "preCalc"):
        require(question.findtext(field) == "true", f"Expected {field}=true")
    subquestions = question.findall("subquestion")
    require(len(subquestions) == 1, "Expected one subquestion")
    subquestion = subquestions[0]
    require(subquestion.findtext("name") == "Q0", "Expected subquestion Q0")
    require(subquestion.findtext("mode") == "6", "Expected subquestion mode 6")
    require(subquestion.findtext("plugininfo") == "Plugin1:", "Expected Plugin1: linkage")
    texts = [node for node in question.findall("text") if node.get("art") == "Questiontext"]
    require(len(texts) == 1, "Expected one Questiontext")
    prompt = texts[0].findtext("inhalt") or ""
    require(prompt.count("[Q0]") == 1, "Question text must contain exactly one [Q0]")
    rendered = QuestionText()
    rendered.feed(prompt)
    require(not re.search(r"\bdataset(?:s|variable)?\b|\bdatens[aä]tz\w*", " ".join(rendered.parts), re.I),
            "Question text must not expose hidden dataset configuration")
    plugin = question.findtext("plugins") or ""
    require(plugin.startswith(PREFIX) and plugin.endswith(SUFFIX), "Invalid Python plugin envelope")
    config = json.loads(plugin[len(PREFIX):-len(SUFFIX)])
    require(isinstance(config, dict), "Plugin configuration must be an object")
    for field in ("datasetVariables", "validation", "indication", "files", "evalConfig",
                  "linterConfig", "linterWeight", "cpuTime", "formatterConfig"):
        require(field in config, f"Missing plugin field: {field}")
    check_python(config["indication"], "indication")
    tree = check_python(config["validation"], "validation")
    checker = [node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "Checker"]
    require(len(checker) == 1, "Expected a Checker class")
    require(any(isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
                for node in checker[0].body), "Checker has no tests")
    variables = config["datasetVariables"]
    require(isinstance(variables, list), "datasetVariables must be a list")
    names = [variable["name"] for variable in variables]
    require(len(names) == len(set(names)), "Duplicate plugin dataset variable")
    require(all(isinstance(name, str) and name.isidentifier() for name in names),
            "Dataset names must be Python identifiers")
    definitions = question.findall("dataset")
    defined_names = [definition.findtext("name") for definition in definitions]
    require(len(defined_names) == len(set(defined_names)), "Duplicate XML dataset")
    require(set(names) == set(defined_names), "Plugin and XML dataset names differ")
    columns = {}
    for variable in variables:
        name = variable["name"]
        require(variable.get("unit") == "", f"{name}: plugin unit must be empty")
        require("{" + name + "}" in prompt, f"{name}: missing question placeholder")
        definition = definitions[defined_names.index(name)]
        require(not definition.findtext("einheit"), f"{name}: XML unit must be empty")
        require(definition.findtext("type") == "calculated", f"{name}: expected calculated dataset")
        values = (definition.findtext("items") or "").split(";")
        require(len(values) == int(definition.findtext("itemcount")), f"{name}: item count mismatch")
        low = number(definition.findtext("minimum"))
        high = number(definition.findtext("maximum"))
        numeric = [number(value) for value in values]
        require(all(low <= value <= high for value in numeric), f"{name}: item outside bounds")
        require(numeric[0] == number(variable["value"]), f"{name}: first item differs from preview")
        columns[name] = [int(value) if value == value.to_integral_value() else float(value)
                         for value in numeric]
    counts = {len(column) for column in columns.values()}
    require(len(counts) <= 1, "Dataset column lengths differ")
    count = next(iter(counts), 1)
    rows = [{name: column[index] for name, column in columns.items()} for index in range(count)]
    return config, rows


def check_export(path, title=None):
    root = ET.parse(path).getroot()
    require(root.tag == "letto", "Expected <letto>, not standard Moodle <quiz> XML")
    require(root.get("mode") == "101" and root.get("databaseinfo") == "sql",
            "Expected letto mode=101, databaseinfo=sql")
    questions = root.findall("question")
    if title is not None:
        questions = [question for question in questions if question.findtext("name") == title]
        require(len(questions) == 1, "--question must select exactly one question")
    require(bool(questions), "No questions found")
    return [(question.findtext("name"), *check_question(question)) for question in questions]


def run_validator(config, rows, example, timeout):
    example = Path(example).resolve()
    require((example / "answer.py").is_file(), "Example answer.py is missing")
    require((example / "dataset.py").is_file(), "Example dataset.py is missing")
    check_python((example / "answer.py").read_text(encoding="utf-8"), "answer.py")
    for index, values in enumerate(rows):
        payload = {"validation": config["validation"], "values": values,
                   "defaults": config["datasetVariables"], "check_local_defaults": index == 0}
        try:
            process = subprocess.run(
                [sys.executable, "-X", "utf8", "-B", "-c", WORKER], cwd=example,
                input=json.dumps(payload, ensure_ascii=False), capture_output=True,
                text=True, encoding="utf-8", errors="replace", timeout=timeout,
            )
        except subprocess.TimeoutExpired as error:
            raise ValueError(f"Dataset row {index + 1}: validator timed out") from error
        require(process.returncode == 0,
                f"Dataset row {index + 1}: validator failed\n{process.stdout}{process.stderr}")
    return len(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export", type=Path)
    parser.add_argument("--question", help="Exact title to select in a combined export")
    parser.add_argument("--example", type=Path, help="Run against this local example (one selected question)")
    parser.add_argument("--timeout", type=float, default=10, help="Seconds per dataset row (default: 10)")
    args = parser.parse_args()
    try:
        require(args.timeout > 0, "Timeout must be positive")
        checked = check_export(args.export, args.question)
        if args.example:
            require(len(checked) == 1, "Use --question to select one question with --example")
        for title, config, rows in checked:
            message = f"{title}: syntax and {len(rows)} dataset rows checked"
            if args.example:
                count = run_validator(config, rows, args.example, args.timeout)
                message += f"; validator passed all {count} rows"
            print(message)
    except (ValueError, KeyError, TypeError, SyntaxError, OSError, ET.ParseError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
