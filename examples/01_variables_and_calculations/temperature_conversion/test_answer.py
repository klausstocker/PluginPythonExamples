"""Unit tests for the temperature conversion example."""

import unittest

import answer

def fahrenheit_to_celsius(temperature_fahrenheit):
    """Convert a Fahrenheit measurement to degrees Celsius."""
    temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
    return temperature_celsius

def celsius_to_fahrenheit(temperature_celsius):
    """Convert a Celsius measurement to degrees Fahrenheit."""
    temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
    return temperature_fahrenheit

class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_converts_celsius_to_fahrenheits(self):
        self.assertAlmostEqual(answer.celsius_to_fahrenheit(0.0), celsius_to_fahrenheit(0.0))
        self.assertAlmostEqual(answer.celsius_to_fahrenheit(37.0), celsius_to_fahrenheit(37.0))
        self.assertAlmostEqual(answer.celsius_to_fahrenheit(-10.0), celsius_to_fahrenheit(-10.0))

    def test_converts_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(answer.fahrenheit_to_celsius(0.0), fahrenheit_to_celsius(0.0))
        self.assertAlmostEqual(answer.fahrenheit_to_celsius(37.0), fahrenheit_to_celsius(37.0))
        self.assertAlmostEqual(answer.fahrenheit_to_celsius(-10.0), fahrenheit_to_celsius(-10.0))

if __name__ == "__main__":
    unittest.main()
