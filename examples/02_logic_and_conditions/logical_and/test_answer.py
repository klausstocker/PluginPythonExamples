"""Tests für die logische Verknüpfung mit and."""

import unittest
import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_neither_limit_reached(self):
        self.assertIs(answer.pruefe_messwerte(42, 6.5), False)

    def test_only_temperature_limit_reached(self):
        self.assertIs(answer.pruefe_messwerte(75, 6.5), False)

    def test_only_current_limit_reached(self):
        self.assertIs(answer.pruefe_messwerte(42, 12.5), False)

    def test_both_limits_exceeded(self):
        self.assertIs(answer.pruefe_messwerte(75, 12.5), True)

    def test_temperature_exactly_at_limit(self):
        self.assertIs(answer.pruefe_messwerte(60, 6.5), False)

    def test_current_exactly_at_limit(self):
        self.assertIs(answer.pruefe_messwerte(42, 10), False)

    def test_both_exactly_at_limits(self):
        self.assertIs(answer.pruefe_messwerte(60, 10), True)

    def test_both_just_below_limits(self):
        self.assertIs(answer.pruefe_messwerte(59.9, 9.9), False)

    def test_temperature_below_current_at_limit(self):
        self.assertIs(answer.pruefe_messwerte(59.9, 10), False)

    def test_temperature_at_limit_current_below(self):
        self.assertIs(answer.pruefe_messwerte(60, 9.9), False)
