"""Unit tests for the motor energy example."""

import unittest

import answer

def calculate_motor_energy_kwh(voltage, current, operating_time_seconds):
    """Return energy in joules for constant voltage and current."""
    power_watts = voltage * current
    energy_kwh = power_watts * operating_time_seconds / 3.6e6
    return energy_kwh

class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_calculates_energy_from_several_measurements(self):
        self.assertAlmostEqual(calculate_motor_energy_kwh(24.0, 1.5, 8.0), answer.calculate_motor_energy_kwh(24.0, 1.5, 8.0))
        self.assertAlmostEqual(calculate_motor_energy_kwh(12.0, 0.75, 20.0), answer.calculate_motor_energy_kwh(12.0, 0.75, 20.0))

if __name__ == "__main__":
    unittest.main()
