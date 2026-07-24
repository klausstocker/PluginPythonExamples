# for_range_datasets example

This beginner-friendly example shows how to use `for number in range(start, stop)` when the `start` and `stop` values come from datasets.

## Learning goal

Learners practice that:

- `range(start, stop)` begins at `start`.
- `range(start, stop)` stops before `stop`.
- a `for` loop can be repeated for several `(start, stop)` datasets.
- nested loops can collect all generated numbers in one list.

## Task

Write a function named `collect_numbers_from_ranges`.

The function receives a list of datasets. Each dataset contains two values:

1. `start` — the first number for `range`.
2. `stop` — the value where `range` stops before reaching it.

For every dataset, use:

```python
for number in range(start, stop):
```

Collect every generated number in a list and return that list.

Example:

```python
datasets = [(1, 4), (6, 9)]
result = collect_numbers_from_ranges(datasets)
print(result)
```

Expected result:

```python
[1, 2, 3, 6, 7, 8]
```

The numbers `4` and `9` are not included because `range(start, stop)` stops before the `stop` value.

## Files

- `answer.py` contains the reference implementation and example datasets.
- `test_answer.py` contains unit tests for `answer.py` using Python's built-in `unittest` framework.

## Run the tests

From the repository root:

```bash
python -m unittest discover -s examples/for_range_datasets -p "test_*.py"
```

Run all examples at once:

```bash
python -m unittest test_all_examples.py
```

## Teaching notes

The example intentionally uses simple tuple datasets such as `(1, 5)`. Teachers can replace these datasets with values from a table, CSV file, or plugin-provided dataset later.
