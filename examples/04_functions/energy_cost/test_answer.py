"""Prüfe Rückgabewerte mit anderen Daten als in der Demonstration."""

import unittest

import answer


class Checker(unittest.TestCase):
    def test_calculations(self):
        cases = [((2.5,), 0.75), ((2.5, 0.4), 1.0), ((0.0,), 0.0), ((3.0, 0.0), 0.0)]
        for arguments, expected in cases:
            with self.subTest(arguments=arguments):
                self.assertAlmostEqual(answer.energiekosten(*arguments), expected)


if __name__ == "__main__":
    unittest.main()
