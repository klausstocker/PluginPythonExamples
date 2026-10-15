"""Prüfe TCP-Versatz, lokale Translation, Orientierung und Gelenkgrenzen."""

import math
import unittest

import answer


def correct(r1: float, d: float, r2: float) -> tuple[float, float, float]:
    """Transformiere den lokalen TCP schrittweise: R2, Tx, R1."""
    base_angle_rad = math.radians(r1)
    wrist_angle_rad = math.radians(r2)
    # Erst den TCP um das Handgelenk drehen, dann im Armkoordinatensystem verschieben.
    arm_x = -0.9 * math.sin(wrist_angle_rad) + d
    arm_y = 0.9 * math.cos(wrist_angle_rad)
    # Zuletzt das gesamte Armkoordinatensystem ins Weltkoordinatensystem drehen.
    x = arm_x * math.cos(base_angle_rad) - arm_y * math.sin(base_angle_rad)
    y = arm_x * math.sin(base_angle_rad) + arm_y * math.cos(base_angle_rad)
    return x, y, r1 + r2


class Checker(unittest.TestCase):
    def assert_pose(self, r1, d, r2, expected):
        pose = answer.forward_kinematics(r1, d, r2)
        self.assertIsInstance(pose, tuple)
        self.assertEqual(len(pose), 3)
        for actual, target in zip(pose, expected):
            self.assertAlmostEqual(actual, target)

    def test_axis_aligned_configurations(self):
        for r1, d, r2, expected in [
            (0.0, 3.0, 0.0, (3.0, 0.9, 0.0)),
            (90.0, 4.0, 0.0, (-0.9, 4.0, 90.0)),
            (180.0, 2.0, 0.0, (-2.0, -0.9, 180.0)),
            (-90.0, 5.0, 0.0, (0.9, -5.0, -90.0)),
        ]:
            with self.subTest(r1=r1, d=d, r2=r2):
                self.assert_pose(r1, d, r2, expected)

    def test_wrist_rotates_tcp_offset(self):
        for r2, expected in [
            (90.0, (3.1, 0.0, 90.0)),
            (180.0, (4.0, -0.9, 180.0)),
            (-90.0, (4.9, 0.0, -90.0)),
        ]:
            with self.subTest(r2=r2):
                self.assert_pose(0.0, 4.0, r2, expected)

    def test_relative_wrist_angle(self):
        coordinate = 3.0 / math.sqrt(2.0)
        self.assert_pose(45.0, 3.0, -45.0, (coordinate, coordinate + 0.9, 0.0))

    def test_general_configurations_against_sequential_transformations(self):
        for r1, d, r2 in [(23.0, 2.4, 71.0), (137.0, 6.2, -49.0),
                          (-128.0, 1.8, 212.0), (-37.0, 5.1, -83.0)]:
            with self.subTest(r1=r1, d=d, r2=r2):
                self.assert_pose(r1, d, r2, correct(r1, d, r2))

    def test_extension_boundaries(self):
        self.assert_pose(90.0, 0.0, -90.0, (0.0, 0.9, 0.0))
        self.assert_pose(90.0, 7.0, -90.0, (0.0, 7.9, 0.0))

    def test_orientation_is_not_normalized(self):
        self.assert_pose(360.0, 2.0, 90.0, (1.1, 0.0, 450.0))
        self.assert_pose(-360.0, 2.0, -90.0, (2.9, 0.0, -450.0))

    def test_invalid_extension(self):
        for d in [-0.01, 7.01]:
            with self.subTest(d=d):
                self.assertIsNone(answer.forward_kinematics(30.0, d, 60.0))

    def test_nonfinite_joint_values(self):
        for index in range(3):
            for value in [math.nan, math.inf, -math.inf]:
                joints = [30.0, 4.0, 60.0]
                joints[index] = value
                with self.subTest(index=index, value=value):
                    self.assertIsNone(answer.forward_kinematics(*joints))


if __name__ == "__main__":
    unittest.main()
