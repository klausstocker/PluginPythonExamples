"""Tests für Winkel zwischen dreidimensionalen NumPy-Vektoren."""

import unittest

import numpy as np

import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_known_angles(self):
        cases = [
            ([2.0, 0.0, 0.0], [0.0, 0.0, 5.0], 90.0),
            ([1.0, 2.0, 2.0], [3.0, 6.0, 6.0], 0.0),
            ([1.0, 2.0, 2.0], [-2.0, -4.0, -4.0], 180.0),
            ([2.0, 0.0, 2.0], [0.0, 3.0, 3.0], 60.0),
            ([2.0, 0.0, 2.0], [0.0, -3.0, -3.0], 120.0),
            ([0.0, 0.0, 4.0], [0.0, 5.0, 5.0], 45.0),
        ]
        for components_a, components_b, expected in cases:
            with self.subTest(a=components_a, b=components_b):
                result = answer.winkel_zwischen_vektoren(
                    np.array(components_a, dtype=np.float64),
                    np.array(components_b, dtype=np.float64),
                )
                self.assertIsInstance(result, float)
                self.assertAlmostEqual(result, expected, places=6)

    def test_swapping_vectors_preserves_angle(self):
        vector_a = np.array([2.0, -3.0, 4.0])
        vector_b = np.array([-1.0, 5.0, 2.0])
        self.assertAlmostEqual(
            answer.winkel_zwischen_vektoren(vector_a, vector_b),
            answer.winkel_zwischen_vektoren(vector_b, vector_a),
        )

    def test_positive_scaling_preserves_angle(self):
        vector_a = np.array([2.0, -3.0, 4.0])
        vector_b = np.array([-1.0, 5.0, 2.0])
        self.assertAlmostEqual(
            answer.winkel_zwischen_vektoren(vector_a, vector_b),
            answer.winkel_zwischen_vektoren(2.5 * vector_a, 0.5 * vector_b),
        )

    def test_invalid_vectors(self):
        valid = np.array([2.0, 3.0, 4.0])
        invalid_vectors = [
            np.zeros(3),
            np.array([1.0, 2.0]),
            np.array([1.0, 2.0, 3.0, 4.0]),
            np.array([[1.0], [2.0], [3.0]]),
            np.array([np.nan, 1.0, 2.0]),
            np.array([1.0, np.inf, 2.0]),
        ]
        for invalid in invalid_vectors:
            for vector_a, vector_b in [(invalid, valid), (valid, invalid)]:
                with self.subTest(a=vector_a, b=vector_b):
                    with self.assertRaises(ValueError):
                        answer.winkel_zwischen_vektoren(vector_a, vector_b)

    def test_inputs_are_unchanged(self):
        vector_a = np.array([2.0, -3.0, 4.0])
        vector_b = np.array([-1.0, 5.0, 2.0])
        original_a = vector_a.copy()
        original_b = vector_b.copy()
        answer.winkel_zwischen_vektoren(vector_a, vector_b)
        np.testing.assert_array_equal(vector_a, original_a)
        np.testing.assert_array_equal(vector_b, original_b)


if __name__ == "__main__":
    unittest.main()
