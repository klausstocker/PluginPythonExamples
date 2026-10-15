# AGENTS.md

This repository contains teacher-facing Python plugin examples. The examples are intended to demonstrate what is possible with the plugin and to give teachers a practical starting point for designing their own examples.

## Repository purpose

- Treat this repository as an examples and teaching-material repository, not as the core plugin implementation.
- Keep examples easy to understand, copy, adapt, and run locally.
- Prefer clear educational structure over clever or overly compact code.
- Assume future contributors may be teachers with limited time and mixed programming experience.

## Expected example structure

Each example should live in its own folder below `examples/<chapter>/` and should usually contain:

- `README.md` — explains the task, learning goal, files, and how to run the tests.
- `answer.py` — contains the reference or example implementation.
- `test_answer.py` — contains tests for the example, preferably using Python's built-in `unittest` framework unless the repository documentation says otherwise.

Keep examples self-contained whenever practical. Avoid requiring shared hidden context unless it is documented clearly in the example README.

## Writing and editing examples

- Use simple, readable Python that is appropriate for learners.
- Prefer explicit names over abbreviations.
- Keep comments helpful and educational, but do not over-comment obvious code.
- Tests should verify the intended learning outcome and should use data that is not identical to the demonstration data in `answer.py` when possible.
- Do not add unnecessary external dependencies. If a dependency is needed, add it to `requirements.txt` and explain why it is needed.
- Keep example READMEs consistent so teachers can quickly compare and adapt examples.

## LeTTo Python questions

- Before creating or changing a LeTTo Python question or its XML export, read and use [.agents/skills/letto-python-question/SKILL.md](.agents/skills/letto-python-question/SKILL.md).
- Use the latest user-corrected `.lto` file as the format reference. Preserve user changes and update only the requested examples.
- Do not use `input()`. Read values through `dataset.<name>.value`; use the existing `DatasetVariable` class in local `dataset.py` files, with an explicit empty unit string. Do not use `SimpleNamespace`.
- Keep dataset units empty in Python, plugin JSON (`"unit": ""`), and XML (`<einheit/>`). Units may appear in task text and program output.
- Student-facing question text must not mention dataset variables, the `dataset` module, or how hidden values are accessed. Present the given quantities naturally through LeTTo placeholders. Keep dataset setup instructions in teacher documentation only.
- Default `linterConfig` for new or updated questions: `--disable=all --enable=F,E,W`. Preserve an explicit user-requested per-question override.
- Tests for these questions use the current values from `dataset.py`, without replacing them with fixed test values. Compare the submission output with a reference implementation. This takes precedence over the general preference for separate test data above.
- Keep the full reference solution in `answer.py`, a starter in plugin `indication`, and grading code in `validation`. The target provides `dataset` and `helpers.RedirectedStdout`; local examples use `examples/common.py`.
- Keep the question text, local defaults, plugin dataset configuration, XML datasets, and the affected combined-export entry consistent. Document local helper dependencies.

## Running tests

Before committing changes, run the tests for any changed example. Typical commands are:

```bash
python -m unittest test_answer.py
```

from inside an example folder, or:

```bash
python -m unittest discover -s examples/<chapter>/<example_name> -p "test_*.py"
```

from the repository root.

If you change shared setup files such as `requirements.txt` or repository-level documentation, also run all available example tests when practical:

```bash
python -m unittest test_all_examples.py
```

## Documentation expectations

- Document every example from the perspective of a teacher who wants to reuse it.
- Include the learning goal, the task statement, and test instructions.
- Mention any assumptions, dependencies, or environment requirements.
- Keep language concise and practical.

## What not to do

- Do not move examples back into the core plugin repository as part of normal example work.
- Do not introduce plugin implementation changes here unless this repository explicitly grows tooling for examples.
- Do not remove existing examples unless the task explicitly asks for it.
- Do not replace simple standard-library solutions with heavier third-party frameworks without a clear reason.
