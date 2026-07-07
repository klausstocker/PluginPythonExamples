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
│   └── minimum_bmi/
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

The examples are designed so that each one can be run with a single Python command from the repository root.

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
You can also run an example from inside its folder:

```bash
cd examples/calculate_sum
python -m unittest test_answer.py
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
