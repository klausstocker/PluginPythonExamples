"""Prüfe Zielorientierung, TCP-Versatz, Erreichbarkeit und den Ursprung."""

import math
import unittest

import answer


def forward_pose(r1: float, d: float, r2: float) -> tuple[float, float, float]:
    """Unabhängige Kontrolle durch schrittweise Vorwärtstransformation des TCP."""
    base_angle_rad = math.radians(r1)
    wrist_angle_rad = math.radians(r2)
    arm_x = d - 0.9 * math.sin(wrist_angle_rad)
    arm_y = 0.9 * math.cos(wrist_angle_rad)
    x = arm_x * math.cos(base_angle_rad) - arm_y * math.sin(base_angle_rad)
    y = arm_x * math.sin(base_angle_rad) + arm_y * math.cos(base_angle_rad)
    return x, y, r1 + r2


class Checker(unittest.TestCase):
    def assert_target(self, x, y, phi):
        joints = answer.inverse_kinematics(x, y, phi)
        self.assertIsInstance(joints, tuple)
        self.assertEqual(len(joints), 3)
        r1, d, r2 = joints
        self.assertGreaterEqual(d, 0.0)
        self.assertLessEqual(d, 7.0)
        self.assertGreaterEqual(r1, -180.0)
        self.assertLessEqual(r1, 180.0)
        for actual, expected in zip(forward_pose(r1, d, r2), (x, y, phi)):
            self.assertAlmostEqual(actual, expected)
        return joints

    def test_known_joint_values(self):
        r1, d, r2 = self.assert_target(-0.9, 4.0, 90.0)
        self.assertAlmostEqual(r1, 90.0)
        self.assertAlmostEqual(d, 4.0)
        self.assertAlmostEqual(r2, 0.0)

    def test_same_position_with_different_orientations(self):
        extensions = []
        for phi in [0.0, 90.0, 180.0, 270.0]:
            with self.subTest(phi=phi):
                r1, d, r2 = self.assert_target(2.0, 3.0, phi)
                extensions.append(d)
        self.assertNotAlmostEqual(extensions[0], extensions[1])

    def test_targets_in_all_quadrants(self):
        for x, y, phi in [(2.1, 1.3, 35.0), (-2.4, 3.2, -70.0),
                          (-3.1, -1.8, 140.0), (3.3, -2.2, -25.0)]:
            with self.subTest(x=x, y=y, phi=phi):
                self.assert_target(x, y, phi)

    def test_extension_upper_boundary(self):
        for r1, r2 in [(0.0, 0.0), (37.0, 82.0), (-143.0, -61.0)]:
            x, y, phi = forward_pose(r1, 7.0, r2)
            with self.subTest(r1=r1, r2=r2):
                actual_r1, d, actual_r2 = self.assert_target(x, y, phi)
                self.assertAlmostEqual(d, 7.0)
                self.assertAlmostEqual(actual_r1, r1)
                self.assertAlmostEqual(actual_r2, r2)

    def test_zero_extension_chooses_zero_base_angle(self):
        for x, y, phi in [(0.0, 0.9, 0.0), (-0.9, 0.0, 90.0),
                          (0.0, -0.9, 180.0), (0.9, 0.0, -90.0)]:
            with self.subTest(phi=phi):
                r1, d, r2 = self.assert_target(x, y, phi)
                self.assertEqual(r1, 0.0)
                self.assertEqual(d, 0.0)
                self.assertEqual(r2, phi)

    def test_tcp_at_origin_is_reachable(self):
        r1, d, r2 = self.assert_target(0.0, 0.0, 0.0)
        self.assertAlmostEqual(r1, -90.0)
        self.assertAlmostEqual(d, 0.9)
        self.assertAlmostEqual(r2, 90.0)

    def test_orientation_is_not_normalized(self):
        self.assert_target(2.0, 1.0, 450.0)
        self.assert_target(-2.0, 1.0, -450.0)

    def test_reachability_depends_on_wrist_position(self):
        self.assert_target(7.8, 0.0, -90.0)
        self.assertIsNone(answer.inverse_kinematics(6.5, 0.0, 90.0))
        self.assertIsNone(answer.inverse_kinematics(7.0001, 0.9, 0.0))

    def test_nonfinite_target_values(self):
        for index in range(3):
            for value in [math.nan, math.inf, -math.inf]:
                target = [2.0, 3.0, 90.0]
                target[index] = value
                with self.subTest(index=index, value=value):
                    self.assertIsNone(answer.inverse_kinematics(*target))


if __name__ == "__main__":
    unittest.main()
