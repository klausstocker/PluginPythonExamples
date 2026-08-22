"""Unit tests for the temperature conversion example."""

import unittest

import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_converts_different_measurements(self):
        self.assertAlmostEqual(answer.celsius_to_fahrenheit(0.0), 32.0)
        self.assertAlmostEqual(answer.celsius_to_fahrenheit(37.0), 98.6)
        self.assertAlmostEqual(answer.celsius_to_fahrenheit(-10.0), 14.0)

    def test_example_result(self):
        self.assertAlmostEqual(answer.example_temperature_fahrenheit, 77.0)


if __name__ == "__main__":
    unittest.main()
