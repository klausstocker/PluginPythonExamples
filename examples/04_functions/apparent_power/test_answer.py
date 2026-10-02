"""Prüfe Rückgabewerte mit anderen Daten als in der Demonstration."""

import unittest

import answer


class Checker(unittest.TestCase):
    def test_calculations(self):
        cases = [((300.0, 400.0), 500.0), ((1200.0, 0.0), 1200.0), ((0.0, 0.0), 0.0), ((300.0, -400.0), 500.0)]
        for arguments, expected in cases:
            with self.subTest(arguments=arguments):
                self.assertAlmostEqual(answer.scheinleistung(*arguments), expected)


if __name__ == "__main__":
    unittest.main()
