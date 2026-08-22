"""Unit tests for the variable basics example."""

import unittest

import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_assignment_and_reassignment(self):
        self.assertEqual(answer.station_name, "Quality control station")

    def test_basic_values_and_types(self):
        self.assertEqual(answer.sample_count, 24)
        self.assertEqual(answer.motor_temperature_celsius, 42.5)
        self.assertEqual(answer.status_message, "Ready")
        self.assertIs(answer.emergency_stop_active, False)
        self.assertIs(answer.sample_count_type, int)
        self.assertIs(answer.motor_temperature_type, float)
        self.assertIs(answer.status_message_type, str)
        self.assertIs(answer.emergency_stop_type, bool)

    def test_sensor_values_are_swapped(self):
        self.assertEqual(answer.left_sensor_state, "clear")
        self.assertEqual(answer.right_sensor_state, "blocked")

    def test_constant_uses_the_given_value(self):
        self.assertEqual(answer.MAX_MOTOR_SPEED_RPM, 3000)


if __name__ == "__main__":
    unittest.main()
