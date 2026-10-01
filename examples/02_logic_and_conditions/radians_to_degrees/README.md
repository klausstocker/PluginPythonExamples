# Radians to degrees, minutes, seconds, and quadrant

## Learning goal

Practice angle units, integer and fractional parts, tuple returns, and modulo
arithmetic when assigning quadrants.

## Task

Implement `rad2degree(angle_rad: float)` and return
`(grad, minuten, sekunden, quadrant)`.

Convert the input from radians to degrees using `math.degrees`. Following the
supplied exercise convention, add 360 degrees repeatedly to negative results
until they are nonnegative. Keep complete turns in positive results: 450 degrees
must remain 450 degrees in `grad`.

Split this value into integer degrees (`grad`), integer arcminutes (`minuten`),
and floating-point arcseconds (`sekunden`). One degree has 60 minutes; one minute
has 60 seconds. Truncate degrees and minutes and retain fractional seconds.

Use `grad % 360` to assign the quadrant:

| Normalized degrees | Quadrant |
| --- | --- |
| 0 inclusive to 90 exclusive | 1 |
| 90 inclusive to 180 exclusive | 2 |
| 180 inclusive to 270 exclusive | 3 |
| 270 inclusive to 360 exclusive | 4 |

For example, `math.radians(32.125)` produces approximately `(32, 7, 30.0, 1)`.
An input of `-math.pi / 2` produces `(270, 0, 0.0, 4)`.

## Assumptions and requirements

- Python 3.9 or newer; only the standard library is needed.
- Inputs are finite floats of classroom-scale magnitude, expressed in radians.
- The asymmetric handling of positive and negative full turns is intentional
  and preserves the supplied reference behavior.
- Floating-point conversion can produce small rounding errors. Do not round
  the result to whole seconds; tests compare seconds with a tolerance.

## Files

- `answer.py`: reference implementation and runnable demonstration.
- `test_answer.py`: deterministic `unittest` checks for units, fractional
  components, axes, quadrants, negative angles, and multiple turns.

## Run and test

From the repository root:

```bash
python examples/02_logic_and_conditions/radians_to_degrees/answer.py
python -m unittest discover -s examples/02_logic_and_conditions/radians_to_degrees -p "test_*.py"
```

Alternatively, from this example folder:

```bash
python -m unittest test_answer.py
```

The repository's `test_all_examples.py` runner discovers this folder automatically.

## Notes for teachers

Give learners this starter as the `QuestionConfigDto.indication`:

```python
def rad2degree(angle_rad: float):
    grad = 0
    minuten = 0
    sekunden = 0
    quadrant = 1
    return grad, minuten, sekunden, quadrant
```

Use `test_answer.py` as `validation`, retaining `Checker` and `rad2degree`.
The supplied `linterConfig` is `--disable=C0114,C0115,C0116`.
Ask students to distinguish radians from degrees and explain the boundary
convention for axes. The tests use known expected values rather than another
copy of the implementation.
