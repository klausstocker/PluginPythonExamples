"""Classify a robot battery using if, elif, and else."""


def battery_status(charge_percent):
    """Return the status of a charge level between 0 and 100 percent."""
    if charge_percent < 20:
        status = "Critical"
    elif charge_percent < 50:
        status = "Charge soon"
    else:
        status = "Ready"
    return status


if __name__ == "__main__":
    print(battery_status(35))
