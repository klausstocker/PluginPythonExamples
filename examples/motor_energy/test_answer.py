"""Unit tests for the motor energy example."""

import unittest

import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_calculates_energy_from_several_measurements(self):
        self.assertAlmostEqual(answer.calculate_motor_energy(24.0, 1.5, 8.0), 288.0)
        self.assertAlmostEqual(answer.calculate_motor_energy(12.0, 0.75, 20.0), 180.0)

    def test_example_result(self):
        self.assertAlmostEqual(answer.example_energy_joules, 1200.0)


if __name__ == "__main__":
    unittest.main()
