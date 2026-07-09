# series_resistors_voltage example

This folder is a self-contained development workspace for a Python plugin example.

## Learning goal

Learners practice writing one small function that calls another function that is already given. The electrical engineering context is resistor color codes and Ohm's law for two resistors connected in series.

## Task

The function `resistance_from_color_bands` is already given. It receives the first color band, second color band, and multiplier band of a resistor, then returns the resistor value in ohms.

For example, these color bands describe a 220 ohm resistor:

```python
resistance_from_color_bands("red", "red", "brown")
```

Write a function named `total_series_voltage` that receives:

- `current_ampere`
- `first_resistor_bands`, a tuple such as `("brown", "black", "brown")`
- `second_resistor_bands`, a tuple such as `("red", "red", "brown")`

The function should use `resistance_from_color_bands` twice: once for the first resistor and once for the second resistor. It should then add the two resistance values and return the total voltage using Ohm's law:

```python
voltage = current * total_resistance
```

For example, if the current is `0.02` amperes and the resistors are `100` ohms and `220` ohms, the total voltage is:

```text
0.02 * (100 + 220) = 6.4 volts
```

## Files

- `answer.py` contains the given helper function and the solution implementation.
- `test_answer.py` contains unit tests for `answer.py` using Python's built-in `unittest` framework.
- The tests check both the returned value and that `total_series_voltage` calls the given `resistance_from_color_bands` function.

## Run the tests

From the repository root:

```bash
python -m unittest discover -s examples/series_resistors_voltage -p "test_*.py"
```

## Visual Studio Code

Use the repository-level VS Code settings to run this example together with the other examples from the **Testing** view. The VS Code test runs through `test_all_examples.py`, so this example can keep using the standalone `import answer` pattern.
