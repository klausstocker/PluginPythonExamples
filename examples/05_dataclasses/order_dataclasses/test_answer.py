"""Vergleiche die zurückgegebenen Dataclass-Objekte mit der Referenzlösung."""

import unittest

import answer


def correct(
    artikel: answer.Artikel, bestellung: answer.Bestellung
) -> answer.Bestellergebnis:
    """Berechne das erwartete Ergebnis mit expliziten Bedingungen."""
    lieferbar = False
    if artikel.aktiv:
        if artikel.bestand >= bestellung.menge:
            lieferbar = True
    return answer.Bestellergebnis(
        bestellung.kunde, artikel.name, bestellung.menge, lieferbar
    )


class Checker(unittest.TestCase):
    def test_order_results(self):
        cases = [
            (answer.Artikel("Heft", 12, True), answer.Bestellung("Ali", 3)),
            (answer.Artikel("Lineal", 4, True), answer.Bestellung("Lea", 4)),
            (answer.Artikel("Mappe", 2, True), answer.Bestellung("Noah", 6)),
            (answer.Artikel("Stift", 10, False), answer.Bestellung("Emma", 2)),
            (answer.Artikel("Radierer", 0, True), answer.Bestellung("Ben", 1)),
            (answer.Artikel("Block", 0, False), answer.Bestellung("Sara", 2)),
        ]
        for artikel, bestellung in cases:
            with self.subTest(artikel=artikel, bestellung=bestellung):
                expected = correct(artikel, bestellung)
                self.assertEqual(
                    answer.bestellung_pruefen(artikel, bestellung), expected
                )


if __name__ == "__main__":
    unittest.main()
