"""Prüfe Armlängen, relative Gelenkwinkel und Positionen in allen Quadranten."""

import math
import unittest

import answer


def correct(alpha: float, beta: float) -> tuple[float, float]:
    """Drehe den Endpunkt aus dem lokalen Koordinatensystem des ersten Arms."""
    alpha_rad = math.radians(alpha)
    beta_rad = math.radians(beta)
    local_x = 100.0 + 80.0 * math.cos(beta_rad)
    local_y = 80.0 * math.sin(beta_rad)
    x = local_x * math.cos(alpha_rad) - local_y * math.sin(alpha_rad)
    y = local_x * math.sin(alpha_rad) + local_y * math.cos(alpha_rad)
    return x, y


class Checker(unittest.TestCase):
    def assert_position(self, alpha, beta, expected):
        position = answer.forward_kinematics(alpha, beta)
        self.assertIsInstance(position, tuple)
        self.assertEqual(len(position), 2)
        for actual, target in zip(position, expected):
            self.assertAlmostEqual(actual, target)

    def test_stretched_arm_in_all_axis_directions(self):
        for alpha, expected in [(0.0, (180.0, 0.0)), (90.0, (0.0, 180.0)),
                                (180.0, (-180.0, 0.0)), (-90.0, (0.0, -180.0))]:
            with self.subTest(alpha=alpha):
                self.assert_position(alpha, 0.0, expected)

    def test_folded_arm(self):
        self.assert_position(90.0, 180.0, (0.0, 20.0))
        self.assert_position(180.0, -180.0, (-20.0, 0.0))

    def test_second_joint_angle_is_relative(self):
        self.assert_position(90.0, 90.0, (-80.0, 100.0))
        self.assert_position(-90.0, -90.0, (-80.0, -100.0))

    def test_oblique_arm_without_rounding(self):
        self.assert_position(30.0, -30.0, (50.0 * math.sqrt(3.0) + 80.0, 50.0))

    def test_general_configurations(self):
        for alpha, beta in [(20.0, 50.0), (150.0, 35.0),
                            (-130.0, -25.0), (-45.0, 12.0)]:
            with self.subTest(alpha=alpha, beta=beta):
                self.assert_position(alpha, beta, correct(alpha, beta))

    def test_angles_beyond_one_revolution(self):
        self.assert_position(450.0, -360.0, (0.0, 180.0))
        self.assert_position(-540.0, 720.0, (-180.0, 0.0))

    def test_nonfinite_angles(self):
        for value in [math.nan, math.inf, -math.inf]:
            with self.subTest(value=value):
                self.assertIsNone(answer.forward_kinematics(value, 20.0))
                self.assertIsNone(answer.forward_kinematics(20.0, value))


if __name__ == "__main__":
    unittest.main()
