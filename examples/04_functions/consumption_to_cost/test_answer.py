"""Prüfe Rückgabewerte mit anderen Daten als in der Demonstration."""

import unittest

import answer


class Checker(unittest.TestCase):
    def test_calculations(self):
        cases = [((750.0, 4.0), 0.9), ((500.0, 3.0, 0.4), 0.6), ((0.0, 2.0), 0.0), ((600.0, 0.0, 0.25), 0.0)]
        for arguments, expected in cases:
            with self.subTest(arguments=arguments):
                self.assertAlmostEqual(answer.betriebskosten(*arguments), expected)

    def test_energy_function(self):
        self.assertAlmostEqual(answer.energie_kwh(400.0, 2.0), 0.8)

    def test_cost_function_default_and_explicit_price(self):
        self.assertAlmostEqual(answer.energiekosten(2.0), 0.6)
        self.assertAlmostEqual(answer.energiekosten(2.0, 0.45), 0.9)


if __name__ == "__main__":
    unittest.main()
