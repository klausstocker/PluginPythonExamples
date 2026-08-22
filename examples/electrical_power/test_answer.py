"""Unit tests for the electrical power example."""

import unittest

import answer

def calculate_power(voltage: float, current: float) -> float:
    """Return electrical power in watts using the correct formula."""
    return voltage * current

class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_calculates_power_from_different_measurements(self):
        self.assertAlmostEqual(calculate_power(12.0, 2.25), answer.calculate_power(12.0, 2.25))
        self.assertAlmostEqual(calculate_power(230.0, 0.4), answer.calculate_power(230.0, 0.4))

if __name__ == "__main__":
    unittest.main()
