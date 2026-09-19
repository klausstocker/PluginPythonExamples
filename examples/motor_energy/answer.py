"""Reference solution for calculating a motor's electrical energy use."""


def calculate_motor_energy_kwh(voltage, current, operating_time_seconds):
    """Return energy in kwh for constant voltage and current."""
    power_watts = voltage * current
    energy_kwh = power_watts * operating_time_seconds / 3.6e6
    return energy_kwh

