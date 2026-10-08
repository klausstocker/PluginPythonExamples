"""Prüfe alle 64 Rückgabewerte der 16 logischen Funktionen."""

import unittest

import answer


def correct(variante: int, a: bool, b: bool) -> bool:
    """Lies das Ausgangsbit in der Zeilenfolge 00, 01, 10, 11."""
    ausgangsbits = format(variante, "04b")
    zeilenindex = 2 * int(a) + int(b)
    return ausgangsbits[zeilenindex] == "1"


class Checker(unittest.TestCase):
    def test_all_variants_and_inputs(self):
        for variante in range(16):
            funktion = getattr(answer, f"funktion_{variante}")
            for a in [False, True]:
                for b in [False, True]:
                    with self.subTest(variante=variante, a=a, b=b):
                        self.assertIs(funktion(a, b), correct(variante, a, b))


if __name__ == "__main__":
    unittest.main()
