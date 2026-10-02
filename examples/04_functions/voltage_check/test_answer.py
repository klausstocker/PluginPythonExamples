"""Prüfe Rückgabewerte mit anderen Daten als in der Demonstration."""

import unittest

import answer


class Checker(unittest.TestCase):
    def test_calculations(self):
        cases = [((210.0,), True), ((250.0,), True), ((209.9,), False), ((250.1,), False), ((215.0, 220.0), False), ((220.0, 220.0), True), ((12.0, 11.0, 13.0), True), ((13.1, 11.0, 13.0), False), ((12.0, 12.0, 12.0), True)]
        for arguments, expected in cases:
            with self.subTest(arguments=arguments):
                self.assertIs(answer.spannung_im_bereich(*arguments), expected)


if __name__ == "__main__":
    unittest.main()
