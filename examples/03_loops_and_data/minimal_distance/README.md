# Minimal distance between points

## Learning goal

Practice nested loops, tuple coordinates, Euclidean distance, and finding a
minimum. Learn why a test needs an independently known expected result.

## Task

Implement `minimalDistance(points: list[tuple[float, float]])`.
Each tuple is a point `(x, y)`. Return the shortest Euclidean distance between
two distinct list entries:

```text
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
```

Return `None` if there are fewer than two points. Never compare an entry with
itself. Separate entries with identical coordinates are allowed and have
distance zero. Leave the input list unchanged.

For example, `[(1, 2), (4, 6), (10, 2)]` has a minimal distance of 5.

## Assumptions and requirements

- Python 3.9 or newer; only the standard library is needed.
- Inputs are lists of coordinate pairs containing finite numbers at ordinary
  classroom scales. Validation of other input types is outside this exercise.
- Small lists are intended: the reference solution checks each pair once,
  using quadratic time and constant extra space.
- Floating-point results are compared with a tolerance.

## Files

- `answer.py`: reference implementation and runnable demonstration.
- `test_answer.py`: deterministic `unittest` checks with known distances,
  including empty and singleton inputs, duplicates, and nonadjacent pairs.

## Run and test

From the repository root:

```bash
python examples/03_loops_and_data/minimal_distance/answer.py
python -m unittest discover -s examples/03_loops_and_data/minimal_distance -p "test_*.py"
```

Alternatively, from this example folder:

```bash
python -m unittest test_answer.py
```

The repository's `test_all_examples.py` runner discovers this folder automatically.

## Notes for teachers

The supplied snippet and its test oracle both subtract `p1[1]` from the second
point's x coordinate. The x difference must use `p1[0]`. They also compare every
point with itself; fixing only the coordinate error would therefore return
zero for every nonempty list. This example corrects both issues and defines
the singleton result as `None`, because no pair exists.

Use the supplied buggy snippet as a debugging exercise, or give learners this
starter as the `QuestionConfigDto.indication`:

```python
def minimalDistance(points: list[tuple[float, float]]):
    return None
```

Use `test_answer.py` as `validation`, retaining `Checker` and `minimalDistance`.
The supplied `linterConfig` is `--disable=C0114,C0115,C0116`.
The reference uses `math.hypot(dx, dy)` to calculate the Euclidean distance.
Discuss why copying a buggy implementation into the test oracle cannot detect
its mistakes. These tests replace unseeded random inputs with known examples.
