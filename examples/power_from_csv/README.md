# Instantaneous power from a text file

## Learning goal

Open a file in text mode, select a row, split semicolon-separated fields,
convert text to numbers, and print a calculated result to standard output.

## Task

Write a program in `answer.py` that opens the fixed filename
`measurements.csv` in the current working directory.

The file is a semicolon-separated CSV file with **no header**. Each row contains
exactly two numbers:

```text
voltage_in_volts;current_in_amperes
```

This line describes the format; it is not part of the file. Decimal numbers
use a dot. There are no blank rows, quoted fields, or units in the file.

1. Open `measurements.csv` in text mode (`"r"`) with UTF-8 encoding. Use a
   `with` statement so the file is closed automatically.
2. Read the **12th row**, counting the first row as row 1.
3. Separate its voltage and current using the delimiter `;`.
4. Convert both fields to `float`.
5. Calculate the instantaneous power: `power = voltage * current`.
6. Print only the numerical result in watts on one line to stdout. Do not add
   a label, unit, prompt, or other output, and do not round the result explicitly.

Use Python's text-file operations and string methods for this exercise.
You do not need NumPy or pandas. You may assume the file exists and contains
at least 12 valid rows; error handling is outside the scope of this task.

Hint: `readlines()` returns a list of text lines. The 12th row has index `11`.
The string method `split(";")` separates its two fields.

## Provided measurements

`measurements.csv` contains 24 equally spaced samples covering one period of
approximately sinusoidal voltage and current. The values are generated from
sine waves and rounded to three decimal places, rather than measured hardware
data:

```text
voltage[k] = 12 * sin(2 * pi * k / 24) V
current[k] =  2 * sin(2 * pi * k / 24) A
k = 0, ..., 23
```

The peaks are 12 V and 2 A, and the two signals are in phase. The next sample
would start a new period, so the endpoint is not duplicated. For a 50 Hz signal,
the period would be 20 ms and the sampling interval 20/24 ms.

The 12th row is `3.106;0.518`, so the expected power is approximately
`1.608908` W. This is the instantaneous power of that sample, not the average
power or energy over the period.

## Files and requirements

- `answer.py`: reference program, with a `main()` function.
- `measurements.csv`: example input file.
- `test_answer.py`: tests that execute the program and inspect stdout.

Python 3 is sufficient; only the standard library is needed. Students should
know variables, lists and indices, strings, `float()`, and `print()`.
The `main()` function is an organizational choice in the reference solution;
students may also write a script directly at module level.

## Run and test

Run the program **from this example folder**, because the filename is relative
to the current working directory:

```bash
cd examples/power_from_csv
python answer.py
python -m unittest test_answer.py
```

Alternatively, run the tests from the repository root:

```bash
python -m unittest discover -s examples/power_from_csv -p "test_*.py"
```

## Notes for teachers

The tests provide temporary files under the same fixed filename, with different
measurements to detect hardcoded results and incorrect row selection. They also
check negative and zero power, a file containing exactly 12 rows, and the supplied
sample file. The original CSV is not modified. Output is compared numerically
to allow normal floating-point representation differences.

Using text mode and closing the file with `with` are checked by reviewing the
student's source code. Negative power in a test checks multiplication of signed
samples; the supplied in-phase waveforms themselves produce nonnegative power.
