"""Unit tests for the for_range_datasets example.

Run from this directory with:
    python -m unittest test_answer.py

Or run from the repository root with:
    python -m unittest discover -s examples/for_range_datasets -p "test_*.py"
"""

import unittest

import answer


def correct_implementation(datasets):
    """Expected behavior for collect_numbers_from_ranges."""
    all_numbers = []

    for start, stop in datasets:
        for number in range(start, stop):
            all_numbers.append(number)

    return all_numbers


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_uses_start_and_stop_values_from_datasets(self):
        datasets = [(2, 6), (10, 13)]
        student_result = answer.collect_numbers_from_ranges(datasets)
        expected_result = correct_implementation(datasets)
        self.assertEqual(student_result, expected_result)

    def test_stop_value_is_not_included(self):
        datasets = [(4, 8)]
        student_result = answer.collect_numbers_from_ranges(datasets)
        self.assertEqual(student_result, [4, 5, 6, 7])
        self.assertNotIn(8, student_result, "range(start, stop) stops before stop")

    def test_empty_range_returns_no_numbers(self):
        datasets = [(5, 5), (8, 6)]
        student_result = answer.collect_numbers_from_ranges(datasets)
        self.assertEqual(student_result, [])


if __name__ == "__main__":
    unittest.main()
