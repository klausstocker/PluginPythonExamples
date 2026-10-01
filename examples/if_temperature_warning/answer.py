"""Set a temperature warning using a single if statement."""


def temperature_warning(temperature):
    """Return a warning at 60 degrees Celsius or above."""
    message = "OK"
    if temperature >= 60:
        message = "Temperature warning"
    return message


if __name__ == "__main__":
    print(temperature_warning(72))
