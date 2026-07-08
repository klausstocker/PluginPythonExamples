# animal_food example

## Learning goal

Learners practice simple inheritance with one abstract base class and two child classes.

They also practice using a list that contains different objects with the same base class.

## Task

A pet hotel wants to calculate how much food is needed for all animals.

You are given:

- an abstract base class `Animal`
- a completed class `Dog`

Your tasks are:

1. Write a class named `Cat` that inherits from `Animal`.
2. Implement the method `get_food` for `Cat`.
3. Complete the function `calculate_total_food`.
4. The function should receive a list of animals and return the total food amount in kilograms.

## Food rules

Cats:

- younger than 1 year: 0.2 kg
- 1 year or older: 0.3 kg

Dogs:

- younger than 5 years: 0.4 kg
- 5 years or older: 0.3 kg

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
