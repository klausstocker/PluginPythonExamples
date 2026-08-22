"""Reference solution for calculating electrical power."""

EXAMPLE_VOLTAGE_VOLTS = 24.0
EXAMPLE_CURRENT_AMPERES = 1.5


def calculate_power(voltage, current):
    """Return electrical power in watts using P = U * I."""
    power_watts = voltage * current
    return power_watts


example_power_watts = calculate_power(
    EXAMPLE_VOLTAGE_VOLTS,
    EXAMPLE_CURRENT_AMPERES,
)
