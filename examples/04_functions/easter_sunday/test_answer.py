"""Prüfe Ostertermine mit einer Referenzfunktion und festen Erwartungswerten."""

from datetime import date
import unittest

import answer


def correct(jahr: int) -> date:
    """Berechne den Referenztermin mit der Meeus/Jones/Butcher-Osterformel."""
    if not 1583 <= jahr <= 4099:
        raise ValueError("Das Jahr muss zwischen 1583 und 4099 liegen.")

    mondzyklus = jahr % 19
    jahrhundert, jahr_im_jahrhundert = divmod(jahr, 100)
    schaltjahrhunderte, jahrhundert_rest = divmod(jahrhundert, 4)
    korrektur = (jahrhundert + 8) // 25
    mondkorrektur = (jahrhundert - korrektur + 1) // 3
    epakte = (
        19 * mondzyklus + jahrhundert - schaltjahrhunderte - mondkorrektur + 15
    ) % 30
    schaltjahre, jahres_rest = divmod(jahr_im_jahrhundert, 4)
    sonntag_abstand = (
        32 + 2 * jahrhundert_rest + 2 * schaltjahre - epakte - jahres_rest
    ) % 7
    ausnahme = (mondzyklus + 11 * epakte + 22 * sonntag_abstand) // 451
    datumscode = epakte + sonntag_abstand - 7 * ausnahme + 114
    monat, tag_ab_null = divmod(datumscode, 31)
    return date(jahr, monat, tag_ab_null + 1)


class Checker(unittest.TestCase):
    def test_known_dates(self):
        termine = [
            (1583, 4, 10),
            (1900, 4, 15),
            (2000, 4, 23),
            (2023, 4, 9),
            (2024, 3, 31),
            (2025, 4, 20),
            (2100, 3, 28),
            (4099, 4, 19),
        ]
        for jahr, monat, tag in termine:
            with self.subTest(jahr=jahr):
                self.assertEqual(correct(jahr), date(jahr, monat, tag))
                self.assertEqual(answer.ostersonntag(jahr), date(jahr, monat, tag))

    def test_earliest_and_latest_easter(self):
        self.assertEqual(answer.ostersonntag(1818), date(1818, 3, 22))
        self.assertEqual(answer.ostersonntag(1943), date(1943, 4, 25))

    def test_correction_cases(self):
        for jahr, tag in [(1954, 18), (1981, 19), (2076, 19)]:
            with self.subTest(jahr=jahr):
                self.assertEqual(answer.ostersonntag(jahr), date(jahr, 4, tag))

    def test_calendar_properties(self):
        for jahr in range(1583, 4100):
            with self.subTest(jahr=jahr):
                ergebnis = answer.ostersonntag(jahr)
                self.assertEqual(ergebnis, correct(jahr))
                self.assertIsInstance(ergebnis, date)
                self.assertEqual(ergebnis.year, jahr)
                self.assertEqual(ergebnis.weekday(), 6)  # Montag = 0, Sonntag = 6.
                self.assertGreaterEqual(ergebnis, date(jahr, 3, 22))
                self.assertLessEqual(ergebnis, date(jahr, 4, 25))

    def test_invalid_years(self):
        for jahr in [-1, 0, 1582, 4100, 10000]:
            with self.subTest(jahr=jahr):
                with self.assertRaises(ValueError):
                    correct(jahr)
                with self.assertRaises(ValueError):
                    answer.ostersonntag(jahr)


if __name__ == "__main__":
    unittest.main()
