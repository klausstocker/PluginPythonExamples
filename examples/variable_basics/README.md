# Variable basics example

## Learning goal

Learners practise assigning and reassigning values, choosing descriptive
`snake_case` names, recognising basic Python types, using simple multiple
assignment, swapping values, and writing constants in uppercase.

## Task

Complete `answer.py` so that it stores the given robot-station data. Rename the
station from `"Assembly station"` to `"Quality control station"`, inspect the
four basic types with `type()`, assign both sensor states in one statement, and
swap those states. Treat `MAX_MOTOR_SPEED_RPM` as a constant: its uppercase
name communicates that the value should not be changed.

Variable names may contain letters, digits, and underscores, but may not start
with a digit. Use descriptive `snake_case` names for ordinary variables.

## Files

- `answer.py` contains the reference implementation.
- `test_answer.py` checks the stored values, types, reassignment, and swap.

This example needs only Python's standard library.

## Run the tests

From the repository root:

```bash
python -m unittest discover -s examples/variable_basics -p "test_*.py"
```
