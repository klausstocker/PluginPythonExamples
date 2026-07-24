"""Unit tests for the for_range_datasets example.

Run from this directory with:
    python -m unittest test_answer.py

Or run from the repository root with:
    python -m unittest discover -s examples/for_range_datasets -p "test_*.py"
"""

import unittest
import dataset
import sys
from io import StringIO

class RedirectedStdout:
    """Capture stdout so examples can test printed output with unittest."""

    def __init__(self):
        self._stdout = None
        self._string_io = None

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._string_io = StringIO()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self._stdout

    def __str__(self):
        return self._string_io.getvalue()

def correct_implementation():
    a = int(dataset.a.value)
    n = int(dataset.n.value)
    for i in range(a, a + n + 1):
        print(i)

class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_output(self):
        with RedirectedStdout() as student_out:
            import answer
        with RedirectedStdout() as expected_out:
            correct_implementation()
        self.assertEqual(str(student_out), str(expected_out))


if __name__ == "__main__":
    unittest.main()
