---
name: letto-python-question
description: Create, adapt, export, or validate teacher-facing LeTTo Python questions in this repository, including local example files and MoodleClozeCalc LTO/XML exports.
---

# LeTTo Python questions

Use this skill when creating or changing a LeTTo Python task, its grading code,
dataset configuration, or `.lto`/combined XML export. Preserve the user's latest
corrections and the requested example scope.

## Establish the reference

Read the example and the latest user-edited `.lto` before editing. Compare its
plugin configuration, question text, datasets, and starter with the local files
and the corresponding combined-export entry. Do not replace user changes with
an older generated version.

For export details, read [references/lto-format.md](references/lto-format.md).
[assets/question.lto](assets/question.lto) is a complete temperature-table
example, derived from the edited robot template and checked locally. It is a
fallback when there is no more recent user-supplied reference, not a schema or
proof of a successful import into a live LeTTo instance.

## Write the local example

- Keep `README.md`, `answer.py`, `dataset.py`, and `test_answer.py` together.
- Read values with `int(dataset.name.value)` or `float(dataset.name.value)`.
  No console input and no `SimpleNamespace`.
- Local `dataset.py` imports `DatasetVariable` from `examples/common.py`, as in
  the existing adapted examples. Set values with `DatasetVariable("name", 4, "")`.
  All dataset unit fields are empty; units remain in text/output when useful.
- Execute the exercise on `import answer`, following the target's grading
  pattern. Define requested helper functions before the loop and call them
  inside it. Avoid a main guard around the exercise itself.
- Local tests import `dataset` and `common.RedirectedStdout`. Define
  `correct_implementation()` using the current dataset, then use a class named
  `Checker` to capture `import answer` and compare its output with the reference.
  Do not patch values or hard-code expected output for the preview dataset.
- In the exported validator, use `from helpers import RedirectedStdout`.
  The target supplies both `helpers` and `dataset`; do not export local shims.
- Explain the task, variable meanings, prerequisites, output precision, and
  local test command in concise German. State the dependency on
  `examples/common.py` and its relative folder structure.

## Prepare the export

Follow the reference's `<letto>` / `MoodleClozeCalc` structure. Use the format
reference for fields and the provided asset for an adaptable working example.
Do not turn it into standard Moodle `<quiz>` XML.

Keep a minimal comment or function stub in `indication`, the full solution in
`answer.py`, and the reference plus `Checker` in `validation`. Remove the local
`unittest.main()` block from the exported validator. Keep dataset defaults,
names, empty units, placeholders, bounds, and item rows consistent. New tasks
normally use 40 dataset rows; preserve explicit user choices. Choose bounds
that satisfy termination conditions and other task prerequisites for every row.

Use short question text focused on the task and exact output format. If a fixed
example output is shown, label the particular values it demonstrates. Dataset
placeholders show the actual question values, for example: "Ein Behälter enthält
{fuellstand} Liter; pro Schritt kommen {zufluss} Liter hinzu." Students do not
see the dataset configuration. Never mention dataset variables, the `dataset`
module, hidden variable names as setup instructions, or access through `.value`
in the student-facing text. Explain the quantities in natural language; function
parameters and variables required by the learning task may still be named.
Keep technical dataset documentation in the teacher-facing README sections
outside the task statement. Do not include local setup instructions in questions.

Use `--disable=all --enable=F,E,W` as the default `linterConfig` for new and
updated questions. Preserve an explicit user-requested per-question override.

For a new question, reset copied IDs to `0`; preserve IDs when editing an
existing user-exported question. Update only its matching entry in an existing
combined export, preserving other questions and user edits.

## Verify the result

Run `python -m unittest test_answer.py` in the affected example directory.
Then run from the repository root:

```text
python .agents/skills/letto-python-question/scripts/validate_export.py examples/<chapter>/<example>/Frage_<example>.lto --example examples/<chapter>/<example>
```

The script checks XML, plugin JSON, embedded Python, and dataset consistency,
then runs the validator against `answer.py` for every exported dataset row in
separate processes with target-like dataset/helper modules. It executes grading
and answer code: use it on repository files being worked on. Its timeout is a
wall-clock bound, not a simulation of target linting or CPU accounting.

For a combined file, select the affected title to avoid requiring unrelated
legacy questions to follow new conventions:

```text
python .agents/skills/letto-python-question/scripts/validate_export.py Fragen_Schleifen_LeTTo.xml --question "Temperaturtabelle mit einer Funktion"
```

Check the single and combined entries agree. Report local validation separately
from a real LeTTo import; never imply the latter happened without evidence.
