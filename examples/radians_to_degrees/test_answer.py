"""Deterministic checks for angle conversion and quadrant conventions."""

import math
import unittest

import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def assert_angle(self, angle_rad, expected):
        result = answer.rad2degree(angle_rad)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 4)
        grad, minuten, sekunden, quadrant = result
        self.assertEqual((grad, minuten, quadrant), (expected[0], expected[1], expected[3]))
        self.assertAlmostEqual(sekunden, expected[2], places=7)

    def test_zero(self):
        self.assert_angle(0.0, (0, 0, 0.0, 1))

    def test_axes(self):
        for radians, expected in [
            (math.pi / 2, (90, 0, 0.0, 2)),
            (math.pi, (180, 0, 0.0, 3)),
            (3 * math.pi / 2, (270, 0, 0.0, 4)),
            (2 * math.pi, (360, 0, 0.0, 1)),
        ]:
            with self.subTest(radians=radians):
                self.assert_angle(radians, expected)

    def test_minutes_and_seconds(self):
        self.assert_angle(math.radians(12.5125), (12, 30, 45.0, 1))
        self.assert_angle(math.radians(203.375), (203, 22, 30.0, 3))

    def test_input_is_radians(self):
        self.assert_angle(1.0, (57, 17, 44.80624709636, 1))

    def test_negative_angles(self):
        for degrees, expected in [
            (-22.5, (337, 30, 0.0, 4)),
            (-90, (270, 0, 0.0, 4)),
            (-360, (0, 0, 0.0, 1)),
            (-450, (270, 0, 0.0, 4)),
        ]:
            with self.subTest(degrees=degrees):
                self.assert_angle(math.radians(degrees), expected)

    def test_positive_full_turns_are_retained(self):
        self.assert_angle(math.radians(450), (450, 0, 0.0, 2))
        self.assert_angle(math.radians(765), (765, 0, 0.0, 1))

    def test_quadrant_interiors(self):
        for degrees, quadrant in [(45, 1), (135, 2), (225, 3), (315, 4)]:
            with self.subTest(degrees=degrees):
                self.assert_angle(math.radians(degrees), (degrees, 0, 0.0, quadrant))

    def test_near_quadrant_boundaries(self):
        for degrees, expected in [
            (89.75, (89, 45, 0.0, 1)),
            (90.25, (90, 15, 0.0, 2)),
            (179.75, (179, 45, 0.0, 2)),
            (180.25, (180, 15, 0.0, 3)),
            (269.75, (269, 45, 0.0, 3)),
            (270.25, (270, 15, 0.0, 4)),
            (359.75, (359, 45, 0.0, 4)),
        ]:
            with self.subTest(degrees=degrees):
                self.assert_angle(math.radians(degrees), expected)


if __name__ == "__main__":
    unittest.main()
