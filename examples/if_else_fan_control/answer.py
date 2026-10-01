"""Choose a fan command using if and else."""


def fan_command(temperature):
    """Return ON at 40 degrees Celsius or above, otherwise OFF."""
    if temperature >= 40:
        command = "ON"
    else:
        command = "OFF"
    return command


if __name__ == "__main__":
    print(fan_command(48))
