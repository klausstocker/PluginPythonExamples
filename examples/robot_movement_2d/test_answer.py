"""Tests for single movements and routes in a fixed 2D coordinate system."""

import unittest

import numpy as np

import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def assert_position(self, result, expected):
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, (2,))
        np.testing.assert_allclose(result, expected, rtol=1e-9, atol=1e-9)

    def test_single_movement_with_fractional_duration(self):
        start = np.array([-2.0, 5.0])
        velocity = np.array([1.5, -2.0])
        self.assert_position(answer.end_position(start, velocity, 2.5), [1.75, 0.0])

    def test_single_stationary_movements(self):
        start = np.array([4.0, -3.0])
        for velocity, duration in [(np.array([2.0, -1.0]), 0.0),
                                   (np.zeros(2), 7.0)]:
            with self.subTest(velocity=velocity, duration=duration):
                self.assert_position(answer.end_position(start, velocity, duration), start)

    def test_single_movement_preserves_inputs(self):
        start = np.array([3.0, -4.0])
        velocity = np.array([-2.0, 0.5])
        result = answer.end_position(start, velocity, 3.0)
        np.testing.assert_array_equal(start, [3.0, -4.0])
        np.testing.assert_array_equal(velocity, [-2.0, 0.5])
        self.assertFalse(np.shares_memory(result, start))
        self.assertFalse(np.shares_memory(result, velocity))

    def test_route_uses_absolute_directions(self):
        start = np.array([2.0, -3.0])
        movements = [(90.0, 2.0, 1.5), (180.0, 0.5, 4.0), (0.0, 3.0, 0.5)]
        self.assert_position(answer.end_position_after_movements(start, movements), [1.5, 0.0])

    def test_diagonal_route(self):
        start = np.array([-1.0, 2.0])
        movements = [(30.0, 4.0, 0.5), (150.0, 2.0, 1.0)]
        self.assert_position(answer.end_position_after_movements(start, movements), [-1.0, 4.0])

    def test_negative_and_wrapped_angles(self):
        for angle in [-90.0, 270.0, 630.0]:
            with self.subTest(angle=angle):
                result = answer.end_position_after_movements(
                    np.array([3.0, 4.0]), [(angle, 1.5, 2.0)]
                )
                self.assert_position(result, [3.0, 1.0])

    def test_closed_route(self):
        start = np.array([-4.0, 1.0])
        movements = [(0.0, 2.0, 2.0), (90.0, 1.0, 3.0),
                     (180.0, 4.0, 1.0), (270.0, 3.0, 1.0)]
        self.assert_position(answer.end_position_after_movements(start, movements), start)

    def test_stationary_segments(self):
        movements = [(40.0, 0.0, 8.0), (120.0, 5.0, 0.0), (180.0, 2.0, 1.5)]
        result = answer.end_position_after_movements(np.array([5.0, 6.0]), movements)
        self.assert_position(result, [2.0, 6.0])

    def test_empty_route_returns_independent_array(self):
        start = np.array([7.0, -2.0])
        result = answer.end_position_after_movements(start, [])
        self.assert_position(result, start)
        self.assertFalse(np.shares_memory(result, start))

    def test_route_preserves_inputs(self):
        start = np.array([2.0, 3.0])
        movements = [(60.0, 1.0, 2.0), (180.0, 2.0, 3.0)]
        original_movements = movements.copy()
        result = answer.end_position_after_movements(start, movements)
        np.testing.assert_array_equal(start, [2.0, 3.0])
        self.assertEqual(movements, original_movements)
        self.assertFalse(np.shares_memory(result, start))


if __name__ == "__main__":
    unittest.main()
