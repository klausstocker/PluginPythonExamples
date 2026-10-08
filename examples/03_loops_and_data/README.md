# 3. Loops and data

Practice repeating calculations, processing collections, and reading measured
values from a file. Learners should already understand variables, comparisons,
and conditions. Introduce lists, tuples, and file access as each task needs them.

## Recommended order

1. [Range datasets](for_range_datasets/README.md): iterate over ranges and collect results.
2. [Count dial stops at zero](count_pointing_at_zero/README.md): process instructions and update a running state.
3. [Minimum BMI](minimum_bmi/README.md): search structured records for the smallest calculated value.
4. [Minimal distance](minimal_distance/README.md): compare pairs of points using nested loops.
5. [Power from CSV](power_from_csv/README.md): read measurements from a file and calculate average power.

[Filter people](filter_people/README.md) is an additional exercise on tuple
unpacking, age comparisons, and filtering with `or`; print matching names to stdout.

[SQLite library](sqlite_library/README.md) introduces a many-to-many relationship
with books, customers, and lends; query who borrowed a book and on which dates.

Each example documents its input format, assumptions, and required concepts.
Keep any accompanying data files with the example when copying it.

## Run tests

From the repository root, for example:

```bash
python -m unittest discover -s examples/03_loops_and_data/minimum_bmi -p "test_*.py"
```

Each example README gives its task and test command. Run all chapters with
`python -m unittest test_all_examples.py`.

Previous: [Logic and conditions](../02_logic_and_conditions/README.md).
