"""Prüfe Winkelumrechnung, Rückgabewerte und verschiedene Aufrufe."""

import math
import unittest

import answer


def correct(
    abstand_m: float, winkel_grad: float, messhoehe_m: float = 1.5
) -> float:
    """Referenzlösung für die erwartete Turmhöhe in Metern."""
    winkel_rad = math.radians(winkel_grad)
    hoehenunterschied_m = abstand_m * math.tan(winkel_rad)
    return hoehenunterschied_m + messhoehe_m


class Checker(unittest.TestCase):
    def test_calculations(self):
        cases = [
            (12.0, 45.0, 2.0),
            (9.0, 30.0, 0.0),
            (4.0, 60.0, 1.2),
            (17.5, 28.0, 1.6),
        ]
        for arguments in cases:
            with self.subTest(arguments=arguments):
                self.assertAlmostEqual(
                    answer.turmhoehe(*arguments), correct(*arguments)
                )

    def test_default_measurement_height(self):
        self.assertAlmostEqual(answer.turmhoehe(8.0, 45.0), correct(8.0, 45.0))

    def test_horizontal_line_of_sight(self):
        self.assertAlmostEqual(
            answer.turmhoehe(15.0, 0.0, 1.8), correct(15.0, 0.0, 1.8)
        )

    def test_repeated_calls_use_their_own_arguments(self):
        first_height = answer.turmhoehe(6.0, 45.0, 1.0)
        second_height = answer.turmhoehe(11.0, 45.0, 2.0)
        self.assertAlmostEqual(first_height, correct(6.0, 45.0, 1.0))
        self.assertAlmostEqual(second_height, correct(11.0, 45.0, 2.0))

    def test_named_arguments_in_different_order(self):
        height = answer.turmhoehe(
            messhoehe_m=2.0, winkel_grad=45.0, abstand_m=7.0
        )
        self.assertAlmostEqual(height, correct(7.0, 45.0, 2.0))


if __name__ == "__main__":
    unittest.main()
