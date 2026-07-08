# example_name example

Replace `example_name` with a short, descriptive folder name such as `calculate_average`.

## Learning goal

Describe what learners should understand or practice after completing this example.

## Task

Write a function named `example_function` that receives one value and returns it unchanged.

Change this task statement to match your real classroom activity.

## Files

- `answer.py` contains the reference or example implementation.
- `test_answer.py` contains unit tests for `answer.py` using Python's built-in `unittest` framework.

## Run the tests

From the repository root, after copying this folder into `examples/example_name`:

```bash
python -m unittest discover -s examples/example_name -p "test_*.py"
```

## Visual Studio Code

After copying this folder into `examples/`, the repository-level VS Code settings can run the new example through `test_all_examples.py` from the **Testing** view while preserving the standalone `import answer` pattern.

## Adapting this template

1. Rename the folder.
2. Rename `example_function` in both Python files.
3. Replace the task statement and learning goal above.
4. Update the test data so it checks the skill you want students to practice.
