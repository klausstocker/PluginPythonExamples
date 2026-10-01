"""Check the default result and the inclusive warning threshold."""

import unittest
import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_normal_temperature(self):
        self.assertEqual(answer.temperature_warning(35), "OK")

    def test_below_threshold(self):
        self.assertEqual(answer.temperature_warning(59.9), "OK")

    def test_at_threshold(self):
        self.assertEqual(answer.temperature_warning(60), "Temperature warning")

    def test_above_threshold(self):
        self.assertEqual(answer.temperature_warning(85), "Temperature warning")

    def test_negative_temperature(self):
        self.assertEqual(answer.temperature_warning(-10), "OK")
