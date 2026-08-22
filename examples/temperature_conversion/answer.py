"""Reference solution for converting Celsius to Fahrenheit."""

def fahrenheit_to_celsius(temperature_fahrenheit):
    """Convert a Fahrenheit measurement to degrees Celsius."""
    temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
    return temperature_celsius

def celsius_to_fahrenheit(temperature_celsius):
    """Convert a Celsius measurement to degrees Fahrenheit."""
    temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
    return temperature_fahrenheit

