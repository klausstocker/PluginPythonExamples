# Plugin Python Examples

This repository contains teacher-facing Python examples for a Python plugin workflow. Each example is intentionally small, self-contained, and easy to copy or adapt for a classroom activity.

## Repository layout

```text
.
??? examples/
?   ??? 01_variables_and_calculations/
?   ?   ??? README.md
?   ?   ??? calculate_sum/
?   ?   ??? electrical_power/
?   ?   ??? temperature_conversion/
?   ?   ??? motor_energy/
?   ?   ??? robot_movement_2d/
?   ?   ??? vector_angle_3d/
?   ??? 02_logic_and_conditions/
?   ?   ??? README.md
?   ?   ??? logical_and/
?   ?   ??? logical_or/
?   ?   ??? logical_not/
?   ?   ??? if_temperature_warning/
?   ?   ??? if_else_fan_control/
?   ?   ??? if_elif_battery_status/
?   ?   ??? radians_to_degrees/
?   ??? 03_loops_and_data/
?       ??? README.md
?       ??? for_range_datasets/
?       ??? count_pointing_at_zero/
?       ??? minimum_bmi/
?       ??? minimal_distance/
?       ??? power_from_csv/
??? template/
??? test_all_examples.py
??? agents.md
??? README.md
??? requirements.txt
```

- `examples/` contains three chapters with ready-to-run example folders.
  Start with [variables and calculations](examples/01_variables_and_calculations/README.md),
  continue with [logic and conditions](examples/02_logic_and_conditions/README.md),
  then [loops and data](examples/03_loops_and_data/README.md).
- `examples/common.py` contains shared helpers used by some existing examples.
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

Most examples use only the Python standard library. The [3D vector angle example](examples/01_variables_and_calculations/vector_angle_3d/README.md) uses NumPy for typed arrays, dot products, and vector lengths. Use a virtual environment to install the requirements.

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

Three introductory condition examples build on each other:

| Example | Focus | Test command |
| --- | --- | --- |
| [Temperature warning](examples/02_logic_and_conditions/if_temperature_warning/README.md) | `if` and a default value | `python -m unittest discover -s examples/02_logic_and_conditions/if_temperature_warning -p "test_*.py"` |
| [Fan control](examples/02_logic_and_conditions/if_else_fan_control/README.md) | `if/else` | `python -m unittest discover -s examples/02_logic_and_conditions/if_else_fan_control -p "test_*.py"` |
| [Battery status](examples/02_logic_and_conditions/if_elif_battery_status/README.md) | `if/elif/else` | `python -m unittest discover -s examples/02_logic_and_conditions/if_elif_battery_status -p "test_*.py"` |

Each includes German teaching notes, a runnable reference solution, and tests
for branch decisions and threshold values.

The [Count dial stops at zero example](examples/03_loops_and_data/count_pointing_at_zero/README.md)
practices loops, string parsing, and modulo arithmetic:

```bash
python -m unittest discover -s examples/03_loops_and_data/count_pointing_at_zero -p "test_*.py"
```

```bash
python -m unittest discover -s examples/01_variables_and_calculations/calculate_sum -p "test_*.py"
```

```bash
python -m unittest discover -s examples/03_loops_and_data/minimum_bmi -p "test_*.py"
```

```bash
python -m unittest discover -s examples/03_loops_and_data/for_range_datasets -p "test_*.py"
```

The [Minimal distance example](examples/03_loops_and_data/minimal_distance/README.md) practices
pairwise comparisons and Euclidean distance:

```bash
python -m unittest discover -s examples/03_loops_and_data/minimal_distance -p "test_*.py"
```

The [Radians to degrees example](examples/02_logic_and_conditions/radians_to_degrees/README.md) covers
degrees, minutes, seconds, and quadrant assignment:

```bash
python -m unittest discover -s examples/02_logic_and_conditions/radians_to_degrees -p "test_*.py"
```

Run all examples at once from the repository root:

```bash
python -m unittest test_all_examples.py
```

The all-example runner discovers `examples/<chapter>/<example>/test_answer.py` and starts a separate Python process in each example folder so every `test_answer.py` can keep using `import answer`.

## Visual Studio Code

This repository includes `.vscode/settings.json` for the VS Code Python extension. Open the repository root in VS Code, select the virtual environment interpreter if you created one, and use the **Testing** view to discover, run, or debug the repository-level `test_all_examples.py` test. That test runs all example folders while preserving their standalone `import answer` imports. The configured unittest discovery command is equivalent to:

```bash
python -m unittest discover -s . -p "test_all_examples.py"
```

## Create a new example from the template

1. Copy the `template/` folder into the appropriate chapter under `examples/` and rename it for your task. Add a link to the chapter README.
2. Edit the copied `README.md` to describe the learning goal, task, files, and test command.
3. Replace the placeholder function in `answer.py` with your reference implementation.
4. Update `test_answer.py` so the tests check the intended learning outcome.
5. Run the new example with one Python command, for example:

```bash
python -m unittest discover -s examples/01_variables_and_calculations/my_new_example -p "test_*.py"
```
