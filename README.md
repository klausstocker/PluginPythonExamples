# Plugin Python Examples

This repository contains teacher-facing Python examples for a Python plugin workflow. Each example is intentionally small, self-contained, and easy to copy or adapt for a classroom activity.

## Repository layout

```text
.
├── examples/
│   ├── calculate_sum/
│   │   ├── README.md
│   │   ├── answer.py
│   │   └── test_answer.py
│   ├── minimum_bmi/
│   │   ├── README.md
│   │   ├── answer.py
│   │   └── test_answer.py
│   └── series_resistors_voltage/
│       ├── README.md
│       ├── answer.py
│       └── test_answer.py
├── template/
│   ├── README.md
│   ├── answer.py
│   └── test_answer.py
├── agents.md
├── README.md
└── requirements.txt
```

- `examples/` contains ready-to-run example folders.
- `template/` contains a simple starting point for creating a new example.
- `requirements.txt` lists Python packages needed to run the examples in a virtual environment.
- `agents.md` documents repository conventions for future contributors.

## Example folder structure

Each example should usually contain:

- `README.md` — explains the task, learning goal, files, and how to run the tests.
- `answer.py` — contains the reference or example implementation.
- `test_answer.py` — contains tests for the example using Python's built-in `unittest` framework.

The examples are designed so each folder can be copied or run on its own with the original `import answer` pattern. The repository also includes a small all-example runner and VS Code settings so the Python extension can run every example test from the Testing view without changing those standalone imports.

## Set up a virtual environment

The examples currently use only the Python standard library, but a virtual environment gives every user a clean, repeatable place to install requirements if dependencies are added later.

From the repository root, run:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the requirements:

```bash
python -m pip install -r requirements.txt
```

When you are finished, deactivate the environment:

```bash
deactivate
```

## Run the examples

Run each example with one Python call from the repository root:

```bash
python -m unittest discover -s examples/calculate_sum -p "test_*.py"
```

```bash
python -m unittest discover -s examples/minimum_bmi -p "test_*.py"
```

```bash
python -m unittest discover -s examples/series_resistors_voltage -p "test_*.py"
```

Run all examples at once from the repository root:

```bash
python -m unittest test_all_examples.py
```

The all-example runner starts a separate Python process in each example folder so every `test_answer.py` can keep using `import answer`.

## Visual Studio Code

This repository includes `.vscode/settings.json` for the VS Code Python extension. Open the repository root in VS Code, select the virtual environment interpreter if you created one, and use the **Testing** view to discover, run, or debug the repository-level `test_all_examples.py` test. That test runs all example folders while preserving their standalone `import answer` imports. The configured unittest discovery command is equivalent to:

```bash
python -m unittest discover -s . -p "test_all_examples.py"
```

## Create a new example from the template

1. Copy the `template/` folder into `examples/` and rename it for your task.
2. Edit the copied `README.md` to describe the learning goal, task, files, and test command.
3. Replace the placeholder function in `answer.py` with your reference implementation.
4. Update `test_answer.py` so the tests check the intended learning outcome.
5. Run the new example with one Python command, for example:

```bash
python -m unittest discover -s examples/my_new_example -p "test_*.py"
```
