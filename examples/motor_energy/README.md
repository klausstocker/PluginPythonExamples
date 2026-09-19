# Motor energy example

## Learning goal

Learners combine several measured quantities and use meaningful variables for
intermediate results in a technical calculation.

## Task

Write `calculate_motor_energy(voltage, current, operating_time_seconds)`.
First calculate electrical power with `power_watts = voltage * current`. Then
calculate and return the energy in joules with
`energy_joules = power_watts * operating_time_seconds`.

## Files

- `answer.py` contains demonstration measurements and the reference solution.
- `test_answer.py` checks the calculation with separate test measurements.

This simplified exercise assumes that voltage and current stay constant. It
needs only Python's standard library.

## Run the tests

```bash
python -m unittest discover -s examples/motor_energy -p "test_*.py"
```
