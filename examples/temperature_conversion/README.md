# Temperature conversion example

## Learning goal

Learners store an intermediate result in a clearly named variable while
converting a temperature measurement.

## Task

Write `celsius_to_fahrenheit(temperature_celsius)`. Use the formula
`fahrenheit = celsius * 9 / 5 + 32`, store the result in
`temperature_fahrenheit`, and return it.

Write `fahrenheit_to_celsius(fahrenheit)`. Store the result in
`temperature_fahrenheit`, and return it.

## Files

- `answer.py` contains a demonstration and the reference implementation.
- `test_answer.py` tests values other than the demonstration value.

This example needs only Python's standard library.

## Run the tests

```bash
python -m unittest discover -s examples/temperature_conversion -p "test_*.py"
```
