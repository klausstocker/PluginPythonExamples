# minimum_bmi example

This folder is a self-contained development workspace for a Python plugin example.

## Learning goal

Learners practice iterating through structured data, calculating a comparison value, and returning the matching item.

## Task

Write a function named `person_with_minimum_bmi` that receives a list of tuples in the form `(name, weight, height)` and returns the name of the person with the minimum BMI. BMI is calculated as `weight / height**2`.

## Files

- `answer.py` contains an example list of tuples and the solution implementation.
- `test_answer.py` contains unit tests for `answer.py` using Python's built-in `unittest` framework.
- The tests intentionally use a different list of tuples than the example data in `answer.py`.

## Run the tests

From the repository root:

```bash
python -m unittest discover -s examples/minimum_bmi -p "test_*.py"
```

## Visual Studio Code

Use the repository-level VS Code settings to discover and run this example together with the other examples from the **Testing** view.
