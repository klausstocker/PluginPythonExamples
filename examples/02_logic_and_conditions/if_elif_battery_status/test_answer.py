"""Check all three charge ranges and their boundaries."""

import unittest
import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_empty_battery(self):
        self.assertEqual(answer.battery_status(0), "Critical")

    def test_low_charge(self):
        self.assertEqual(answer.battery_status(12), "Critical")

    def test_below_first_threshold(self):
        self.assertEqual(answer.battery_status(19.9), "Critical")

    def test_at_first_threshold(self):
        self.assertEqual(answer.battery_status(20), "Charge soon")

    def test_medium_charge(self):
        self.assertEqual(answer.battery_status(32), "Charge soon")

    def test_below_second_threshold(self):
        self.assertEqual(answer.battery_status(49.9), "Charge soon")

    def test_at_second_threshold(self):
        self.assertEqual(answer.battery_status(50), "Ready")

    def test_high_charge(self):
        self.assertEqual(answer.battery_status(78), "Ready")

    def test_full_battery(self):
        self.assertEqual(answer.battery_status(100), "Ready")
