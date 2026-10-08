"""Vergleiche die Rückgabewerte mit einer unabhängigen Referenzlösung."""

import math
import unittest

import answer


def correct(anzahl_zeilen: int) -> str:
    """Baue die Referenzausgabe als String mit Binomialkoeffizienten auf."""
    ausgabe = ""
    for zeilenindex in range(anzahl_zeilen):
        zahlen = []
        for spaltenindex in range(zeilenindex + 1):
            zahlen.append(str(math.comb(zeilenindex, spaltenindex)))
        ausgabe += " ".join(zahlen) + "\n"
    return ausgabe


class Checker(unittest.TestCase):
    def test_output_matches_reference(self):
        for anzahl_zeilen in [0, 1, 2, 4, 7, 12]:
            with self.subTest(anzahl_zeilen=anzahl_zeilen):
                self.assertEqual(
                    answer.pascalsches_dreieck(anzahl_zeilen),
                    correct(anzahl_zeilen),
                )

    def test_repeated_calls_start_with_first_row(self):
        for anzahl_zeilen in [3, 6, 3]:
            with self.subTest(anzahl_zeilen=anzahl_zeilen):
                self.assertEqual(
                    answer.pascalsches_dreieck(anzahl_zeilen),
                    correct(anzahl_zeilen),
                )


if __name__ == "__main__":
    unittest.main()
