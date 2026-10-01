# Count dial stops at zero

## Learning goal

Practice loops, string slicing, input validation, and modulo arithmetic by
tracking a circular dial. This exercise adapts
[Advent of Code 2025, Day 1, Part 1](https://adventofcode.com/2025/day/1).

## Task

Implement `countPointingAt0(start: int, rotations: list[str]) -> int`.
The dial has positions 0 through 99. Each instruction contains `L` (subtract)
or `R` (add), followed by a nonnegative whole-number distance. Positions wrap
around: moving left from 0 reaches 99, and moving right from 99 reaches 0.

Return how many rotations **end at zero**. Passing zero during a rotation does
not count, and the initial position does not count. A rotation of several full
turns contributes at most one stop. A zero-distance rotation counts if the
dial is at zero. An empty list returns 0.

For example, starting at 20 with `["L20", "R15", "L15"]` ends each rotation at
0, 15, and 0, so the result is 2.

## Assumptions and requirements

- Python 3.9 or newer; only the standard library is needed.
- `start` is an integer; raise `ValueError` if it is outside 0 through 99.
- `rotations` is a list of strings. Use uppercase directions and decimal
  digits for distances, without signs, spaces, or decimal points.
- Raise `ValueError` for empty instructions, invalid directions, or missing
  or invalid distances. Distances of 100 or more are allowed.

## Files

- `answer.py`: reference implementation and a runnable demonstration.
- `test_answer.py`: `unittest` checks, including all four supplied cases,
  boundary cases, and invalid inputs.

## Run and test

From the repository root:

```bash
python examples/count_pointing_at_zero/answer.py
python -m unittest discover -s examples/count_pointing_at_zero -p "test_*.py"
```

Alternatively, from this example folder:

```bash
python -m unittest test_answer.py
```

The repository's `test_all_examples.py` runner discovers this folder automatically.

## Notes for teachers

Give learners this starter function:

```python
def countPointingAt0(start: int, rotations: list[str]):
    return 0
```

For `QuestionConfigDto`, use the starter as `indication` and the contents of
`test_answer.py` as `validation`. Keep the function name and the `Checker`
class name unchanged. The supplied `linterConfig` is
`--disable=C0114,C0115,C0116`.

Ask learners to trace the position after each rotation before coding. Discuss
how `% 100` handles negative positions and multiple full turns. The tests call
the student's `answer.countPointingAt0` directly.
