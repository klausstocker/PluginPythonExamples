"""Vergleiche die Rückgabewerte mit unabhängigen Referenzlösungen."""

import unittest

import answer


def correct_ist_primzahl(zahl: int) -> bool:
    """Prüfe zum Vergleich alle möglichen Teiler unterhalb der Zahl."""
    if zahl < 2:
        return False
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
            return False
    return True


def correct(start: int, ende: int) -> list[int]:
    """Berechne die erwartete Primzahlliste."""
    ergebnis = []
    for zahl in range(start, ende + 1):
        if correct_ist_primzahl(zahl):
            ergebnis.append(zahl)
    return ergebnis


class Checker(unittest.TestCase):
    def test_numbers_below_two(self):
        for zahl in [-100, -7, -1, 0, 1]:
            with self.subTest(zahl=zahl):
                self.assertEqual(answer.ist_primzahl(zahl), correct_ist_primzahl(zahl))

    def test_prime_numbers(self):
        for zahl in [2, 3, 5, 7, 11, 29, 97, 101, 997]:
            with self.subTest(zahl=zahl):
                self.assertEqual(answer.ist_primzahl(zahl), correct_ist_primzahl(zahl))

    def test_composite_numbers(self):
        for zahl in [4, 6, 8, 15, 21, 35, 77, 143, 221]:
            with self.subTest(zahl=zahl):
                self.assertEqual(answer.ist_primzahl(zahl), correct_ist_primzahl(zahl))

    def test_prime_squares(self):
        # Der Teiler an der Quadratwurzel muss ebenfalls geprüft werden.
        for zahl in [9, 25, 49, 121, 169, 289]:
            with self.subTest(zahl=zahl):
                self.assertEqual(answer.ist_primzahl(zahl), correct_ist_primzahl(zahl))

    def test_ranges(self):
        cases = [(-5, 7), (0, 1), (2, 2), (4, 4), (3, 13),
                 (14, 16), (31, 53), (90, 130), (8, 3)]
        for start, ende in cases:
            with self.subTest(start=start, ende=ende):
                self.assertEqual(
                    answer.primzahlen_im_bereich(start, ende), correct(start, ende)
                )

    def test_repeated_calls(self):
        for start, ende in [(2, 7), (14, 16), (2, 7)]:
            with self.subTest(start=start, ende=ende):
                self.assertEqual(
                    answer.primzahlen_im_bereich(start, ende), correct(start, ende)
                )


if __name__ == "__main__":
    unittest.main()
