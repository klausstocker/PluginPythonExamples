"""Check pair selection and Euclidean distance using known results."""

import math
import unittest

import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_empty_list(self):
        self.assertIsNone(answer.minimalDistance([]))

    def test_single_point(self):
        self.assertIsNone(answer.minimalDistance([(3.0, 8.0)]))

    def test_two_points_with_different_coordinates(self):
        self.assertAlmostEqual(answer.minimalDistance([(2.0, 7.0), (8.0, 15.0)]), 10.0)

    def test_horizontal_and_vertical_distances(self):
        for points, expected in [
            ([(2.0, 9.0), (7.0, 9.0)], 5.0),
            ([(4.0, -3.0), (4.0, 5.0)], 8.0),
        ]:
            with self.subTest(points=points):
                self.assertAlmostEqual(answer.minimalDistance(points), expected)

    def test_closest_pair_can_be_late_in_list(self):
        points = [(100.0, 100.0), (-50.0, 20.0), (2.0, 3.0), (3.0, 4.0)]
        self.assertAlmostEqual(answer.minimalDistance(points), math.sqrt(2.0))

    def test_closest_pair_can_be_nonadjacent(self):
        points = [(1.0, 4.0), (100.0, 100.0), (1.0, 6.0)]
        self.assertAlmostEqual(answer.minimalDistance(points), 2.0)

    def test_duplicate_entries_have_zero_distance(self):
        points = [(2.0, 8.0), (-3.0, 6.0), (2.0, 8.0)]
        self.assertEqual(answer.minimalDistance(points), 0.0)

    def test_negative_and_fractional_coordinates(self):
        points = [(-1.5, -2.0), (-1.2, -1.6), (10.0, 10.0)]
        self.assertAlmostEqual(answer.minimalDistance(points), 0.5)

    def test_order_does_not_change_result(self):
        points = [(0.0, 5.0), (6.0, 5.0), (6.0, 7.0)]
        self.assertAlmostEqual(answer.minimalDistance(points), 2.0)
        self.assertAlmostEqual(answer.minimalDistance(list(reversed(points))), 2.0)

    def test_input_is_unchanged(self):
        points = [(8.0, 1.0), (2.0, 3.0), (4.0, 9.0)]
        original_points = points.copy()
        answer.minimalDistance(points)
        self.assertEqual(points, original_points)


if __name__ == "__main__":
    unittest.main()
