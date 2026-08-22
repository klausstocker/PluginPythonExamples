"""Unit tests for the electrical power example."""

import unittest

import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_calculates_power_from_different_measurements(self):
        self.assertAlmostEqual(answer.calculate_power(12.0, 2.25), 27.0)
        self.assertAlmostEqual(answer.calculate_power(230.0, 0.4), 92.0)

    def test_example_uses_its_constants(self):
        self.assertAlmostEqual(answer.example_power_watts, 36.0)


if __name__ == "__main__":
    unittest.main()
