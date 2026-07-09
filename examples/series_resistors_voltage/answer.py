"""Reference solution for the series resistors voltage example."""


def resistance_from_color_bands(first_band, second_band, multiplier_band):
    """Return a resistor value in ohms from three resistor color bands."""
    color_digits = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "gray": 8,
        "white": 9,
    }

    first_digit = color_digits[first_band]
    second_digit = color_digits[second_band]
    multiplier = 10 ** color_digits[multiplier_band]

    return (first_digit * 10 + second_digit) * multiplier


def total_series_voltage(current_ampere, first_resistor_bands, second_resistor_bands):
    """Return the total voltage needed for two color-coded resistors in series."""
    first_resistance_ohm = resistance_from_color_bands(*first_resistor_bands)
    second_resistance_ohm = resistance_from_color_bands(*second_resistor_bands)
    total_resistance_ohm = first_resistance_ohm + second_resistance_ohm
    return current_ampere * total_resistance_ohm
