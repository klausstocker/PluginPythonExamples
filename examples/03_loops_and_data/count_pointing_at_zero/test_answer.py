"""Tests for dial endpoints, wraparound, and input validation."""

import unittest

import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_example(self):
        rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        self.assertEqual(answer.countPointingAt0(50, rotations), 3)

    def test_wraparound(self):
        self.assertEqual(answer.countPointingAt0(5, ["L10", "R5"]), 1)

    def test_two_zero_stops(self):
        self.assertEqual(answer.countPointingAt0(50, ["R50", "L1", "R1"]), 2)

    def test_five_zero_stops(self):
        rotations = ["R50", "R100", "L100", "R200", "L300"]
        self.assertEqual(answer.countPointingAt0(50, rotations), 5)

    def test_passing_zero_does_not_count(self):
        self.assertEqual(answer.countPointingAt0(10, ["L20", "R220"]), 0)

    def test_empty_rotations(self):
        for start in [0, 42, 99]:
            with self.subTest(start=start):
                self.assertEqual(answer.countPointingAt0(start, []), 0)

    def test_starting_at_zero_does_not_count(self):
        self.assertEqual(answer.countPointingAt0(0, ["R1"]), 0)

    def test_zero_distance(self):
        self.assertEqual(answer.countPointingAt0(0, ["R0", "L0"]), 2)
        self.assertEqual(answer.countPointingAt0(12, ["R0", "L0"]), 0)

    def test_dial_boundaries(self):
        self.assertEqual(answer.countPointingAt0(99, ["R1"]), 1)
        self.assertEqual(answer.countPointingAt0(0, ["L1", "R1"]), 1)

    def test_invalid_start(self):
        for start in [-1, 100]:
            with self.subTest(start=start):
                with self.assertRaises(ValueError):
                    answer.countPointingAt0(start, [])

    def test_invalid_rotations(self):
        for rotation in ["", "X10", "l10", "10", "L", "R", "R-1", "L+2", "R1.5", "Labc", "R 5", "L5\n"]:
            with self.subTest(rotation=rotation):
                with self.assertRaises(ValueError):
                    answer.countPointingAt0(50, [rotation])


if __name__ == "__main__":
    unittest.main()
