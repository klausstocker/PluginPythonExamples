"""Convert radians to degrees, minutes, seconds, and a quadrant."""

import math


def rad2degree(angle_rad: float) -> tuple[int, int, float, int]:
    """Return (grad, minuten, sekunden, quadrant) using the exercise convention."""
    total_degrees = math.degrees(angle_rad)
    while total_degrees < 0:
        total_degrees += 360.0

    grad = int(total_degrees)
    remaining_minutes = (total_degrees - grad) * 60
    minuten = int(remaining_minutes)
    sekunden = (remaining_minutes - minuten) * 60

    # Keep full turns in grad, but use the direction to find the quadrant.
    normalized_degrees = grad % 360
    quadrant = normalized_degrees // 90 + 1
    return grad, minuten, sekunden, quadrant


if __name__ == "__main__":
    print(rad2degree(math.radians(32.125)))  # (32, 7, 30.0, 1)
