"""Reference solution for calculating a motor's electrical energy use."""

EXAMPLE_VOLTAGE_VOLTS = 48.0
EXAMPLE_CURRENT_AMPERES = 2.5
EXAMPLE_OPERATING_TIME_SECONDS = 10.0


def calculate_motor_energy(voltage, current, operating_time_seconds):
    """Return energy in joules for constant voltage and current."""
    power_watts = voltage * current
    energy_joules = power_watts * operating_time_seconds
    return energy_joules


example_energy_joules = calculate_motor_energy(
    EXAMPLE_VOLTAGE_VOLTS,
    EXAMPLE_CURRENT_AMPERES,
    EXAMPLE_OPERATING_TIME_SECONDS,
)
