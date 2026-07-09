"""Unit tests for the series resistors voltage example.

Run from this directory with:
    python -m unittest test_answer.py

Or run from the repository root with:
    python -m unittest discover -s examples/series_resistors_voltage -p "test_*.py"
"""

import unittest
from unittest.mock import patch

import answer


def correct_implementation(current_ampere, first_resistor_bands, second_resistor_bands):
    """Expected behavior for total_series_voltage."""
    color_digits = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "gray": 8,
        "white": 9,
    }

    first_resistance_ohm = (
        color_digits[first_resistor_bands[0]] * 10 + color_digits[first_resistor_bands[1]]
    ) * 10 ** color_digits[first_resistor_bands[2]]
    second_resistance_ohm = (
        color_digits[second_resistor_bands[0]] * 10
        + color_digits[second_resistor_bands[1]]
    ) * 10 ** color_digits[second_resistor_bands[2]]
    return current_ampere * (first_resistance_ohm + second_resistance_ohm)


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_returns_total_voltage_for_two_series_resistors(self):
        first_resistor = ("brown", "black", "brown")  # 100 ohms
        second_resistor = ("red", "red", "brown")  # 220 ohms

        self.assertEqual(
            answer.total_series_voltage(0.02, first_resistor, second_resistor),
            correct_implementation(0.02, first_resistor, second_resistor),
        )

    def test_returns_total_voltage_for_different_values(self):
        first_resistor = ("yellow", "violet", "black")  # 47 ohms
        second_resistor = ("orange", "orange", "brown")  # 330 ohms

        self.assertEqual(
            answer.total_series_voltage(0.05, first_resistor, second_resistor),
            correct_implementation(0.05, first_resistor, second_resistor),
        )

    def test_uses_given_color_band_function(self):
        calls = []

        def fake_resistance_from_color_bands(first_band, second_band, multiplier_band):
            calls.append((first_band, second_band, multiplier_band))
            if first_band == "brown":
                return 10
            return 20

        with patch(
            "answer.resistance_from_color_bands",
            side_effect=fake_resistance_from_color_bands,
        ):
            result = answer.total_series_voltage(
                0.5,
                ("brown", "black", "brown"),
                ("red", "red", "brown"),
            )

        self.assertEqual(result, 15)
        self.assertEqual(
            calls,
            [("brown", "black", "brown"), ("red", "red", "brown")],
        )
