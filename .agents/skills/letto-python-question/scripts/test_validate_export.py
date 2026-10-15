"""Exercise meaningful export checks and native-style grading failures."""

import ast
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

from validate_export import PREFIX, SUFFIX, check_export, check_question, run_validator


SKILL = Path(__file__).resolve().parents[1]
REPOSITORY = SKILL.parents[2]
ASSET = SKILL / "assets" / "question.lto"


class ExportChecks(unittest.TestCase):
    def setUp(self):
        self.question = ET.parse(ASSET).getroot().find("question")

    def test_complete_asset_has_forty_consistent_rows(self):
        title, config, rows = check_export(ASSET)[0]
        self.assertTrue(title)
        self.assertEqual(len(rows), 40)
        self.assertEqual(rows[0], {item["name"]: item["value"] for item in config["datasetVariables"]})

    def test_malformed_plugin_json_is_rejected(self):
        self.question.find("plugins").text = PREFIX + "{invalid}" + SUFFIX
        with self.assertRaises(ValueError):
            check_question(self.question)

    def test_nonempty_dataset_unit_is_rejected(self):
        self.question.find("dataset/einheit").text = "C"
        with self.assertRaisesRegex(ValueError, "unit must be empty"):
            check_question(self.question)

    def test_hidden_dataset_instructions_in_question_are_rejected(self):
        questiontext = next(node for node in self.question.findall("text")
                            if node.get("art") == "Questiontext")
        questiontext.find("inhalt").text += "<p>Verwende die Dataset-Variablen.</p>"
        with self.assertRaisesRegex(ValueError, "hidden dataset configuration"):
            check_question(self.question)

    def test_dataset_item_count_mismatch_is_rejected(self):
        self.question.find("dataset/itemcount").text = "39"
        with self.assertRaisesRegex(ValueError, "item count mismatch"):
            check_question(self.question)

    def test_out_of_range_dataset_value_is_rejected(self):
        self.question.find("dataset/minimum").text = "1000"
        with self.assertRaisesRegex(ValueError, "outside bounds"):
            check_question(self.question)

    def test_missing_combined_question_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "select exactly one"):
            check_export(ASSET, "Missing question")

    def test_native_validator_accepts_solution_and_rejects_empty_submission(self):
        config, rows = check_question(self.question)
        reference = next(node for node in ast.parse(config["validation"]).body
                         if isinstance(node, ast.FunctionDef) and node.name == "correct_implementation")
        solution = "import dataset\n\n" + ast.unparse(reference) + "\n\ncorrect_implementation()\n"
        directory = tempfile.TemporaryDirectory(prefix="skill-export-test-", dir=REPOSITORY)
        target = Path(directory.name).resolve()
        # Confirm the exact cleanup target is inside this repository before cleanup.
        self.assertTrue(target.is_relative_to(REPOSITORY.resolve()))
        with directory:
            local = "from dataclasses import dataclass\n\n@dataclass\nclass DatasetVariable:\n    value: object\n    unit: str = ''\n\n"
            for item in config["datasetVariables"]:
                local += f"{item['name']} = DatasetVariable({item['value']!r})\n"
            (target / "dataset.py").write_text(local, encoding="utf-8")
            answer = target / "answer.py"
            answer.write_text(solution, encoding="utf-8")
            self.assertEqual(run_validator(config, rows[:1], target, 10), 1)
            answer.write_text("pass\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "validator failed"):
                run_validator(config, rows[:1], target, 10)


if __name__ == "__main__":
    unittest.main()
