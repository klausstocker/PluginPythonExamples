"""Prüfe Gelenkwinkel, Vorwärtskinematik und Arbeitsbereich."""

import math
import unittest

import answer


def correct(x: float, y: float) -> tuple[float, float] | None:
    """Referenzwinkel in Grad für Arme mit 100 mm und 80 mm Länge."""
    if not math.isfinite(x) or not math.isfinite(y):
        return None

    arm_1 = 100.0
    arm_2 = 80.0
    abstand = math.hypot(x, y)
    if not abs(arm_1 - arm_2) <= abstand <= arm_1 + arm_2:
        return None

    # Kosinussatz im Dreieck aus beiden Armen und der Linie zum Zielpunkt.
    cos_schulterwinkel = (
        arm_1**2 + abstand**2 - arm_2**2
    ) / (2 * arm_1 * abstand)
    schulterwinkel = math.acos(max(-1.0, min(1.0, cos_schulterwinkel)))
    alpha = math.atan2(y, x) - schulterwinkel

    cos_innenwinkel = (
        arm_1**2 + arm_2**2 - abstand**2
    ) / (2 * arm_1 * arm_2)
    innenwinkel = math.acos(max(-1.0, min(1.0, cos_innenwinkel)))
    beta = math.pi - innenwinkel
    return math.degrees(alpha), math.degrees(beta)


class Checker(unittest.TestCase):
    def test_known_joint_angles(self):
        alpha, beta = answer.inverse_kinematik(-80.0, 100.0)
        self.assertAlmostEqual(alpha, 90.0)
        self.assertAlmostEqual(beta, 90.0)

    def test_target_positions_in_all_quadrants(self):
        for x, y in [(70.0, 50.0), (-60.0, 90.0), (-90.0, -40.0), (50.0, -110.0)]:
            with self.subTest(x=x, y=y):
                alpha, beta = answer.inverse_kinematik(x, y)
                expected_alpha, expected_beta = correct(x, y)
                self.assertAlmostEqual(alpha, expected_alpha)
                self.assertAlmostEqual(beta, expected_beta)
                self.assertGreaterEqual(beta, 0.0)
                self.assertLessEqual(beta, 180.0)
                alpha_rad = math.radians(alpha)
                beta_rad = math.radians(beta)
                # Die Vorwärtskinematik muss wieder die Zielposition ergeben.
                calculated_x = 100.0 * math.cos(alpha_rad) + 80.0 * math.cos(alpha_rad + beta_rad)
                calculated_y = 100.0 * math.sin(alpha_rad) + 80.0 * math.sin(alpha_rad + beta_rad)
                self.assertAlmostEqual(calculated_x, x)
                self.assertAlmostEqual(calculated_y, y)

    def test_workspace_boundaries(self):
        for x, y, expected_alpha, expected_beta in [
            (180.0, 0.0, 0.0, 0.0),
            (0.0, 180.0, 90.0, 0.0),
            (20.0, 0.0, 0.0, 180.0),
            (0.0, -20.0, -90.0, 180.0),
        ]:
            with self.subTest(x=x, y=y):
                alpha, beta = answer.inverse_kinematik(x, y)
                self.assertAlmostEqual(alpha, expected_alpha)
                self.assertAlmostEqual(beta, expected_beta)
                reference_alpha, reference_beta = correct(x, y)
                self.assertAlmostEqual(alpha, reference_alpha)
                self.assertAlmostEqual(beta, reference_beta)

    def test_unreachable_targets(self):
        for x, y in [(0.0, 0.0), (19.9, 0.0), (180.1, 0.0), (150.0, 150.0)]:
            with self.subTest(x=x, y=y):
                self.assertIsNone(correct(x, y))
                self.assertIsNone(answer.inverse_kinematik(x, y))

    def test_nonfinite_coordinates(self):
        for x, y in [(math.nan, 30.0), (30.0, math.nan), (math.inf, 0.0), (0.0, -math.inf)]:
            with self.subTest(x=x, y=y):
                self.assertIsNone(correct(x, y))
                self.assertIsNone(answer.inverse_kinematik(x, y))


if __name__ == "__main__":
    unittest.main()
