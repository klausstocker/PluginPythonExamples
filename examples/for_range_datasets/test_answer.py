"""Unit tests for the for_range_datasets example.

Run from this directory with:
    python -m unittest test_answer.py

Or run from the repository root with:
    python -m unittest discover -s examples/for_range_datasets -p "test_*.py"
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import dataset
from common import RedirectedStdout


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
