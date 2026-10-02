"""Prüfe Rückgabewerte mit anderen Daten als in der Demonstration."""

import unittest

import answer


class Checker(unittest.TestCase):
    def test_calculations(self):
        cases = [((600.0, 3.0), 1.8), ((125.0, 0.5), 0.0625), ((0.0, 4.0), 0.0), ((250.0, 0.0), 0.0)]
        for arguments, expected in cases:
            with self.subTest(arguments=arguments):
                self.assertAlmostEqual(answer.energie_kwh(*arguments), expected)


if __name__ == "__main__":
    unittest.main()
