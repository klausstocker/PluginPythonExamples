"""Reference solution for converting Celsius to Fahrenheit."""

EXAMPLE_TEMPERATURE_CELSIUS = 25.0


def celsius_to_fahrenheit(temperature_celsius):
    """Convert a Celsius measurement to degrees Fahrenheit."""
    temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
    return temperature_fahrenheit


example_temperature_fahrenheit = celsius_to_fahrenheit(
    EXAMPLE_TEMPERATURE_CELSIUS
)
