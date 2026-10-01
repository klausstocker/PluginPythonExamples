"""Check both fan commands and the switching threshold."""

import unittest
import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_cool_temperature(self):
        self.assertEqual(answer.fan_command(22), "OFF")

    def test_below_threshold(self):
        self.assertEqual(answer.fan_command(39.9), "OFF")

    def test_at_threshold(self):
        self.assertEqual(answer.fan_command(40), "ON")

    def test_above_threshold(self):
        self.assertEqual(answer.fan_command(55), "ON")

    def test_negative_temperature(self):
        self.assertEqual(answer.fan_command(-5), "OFF")
