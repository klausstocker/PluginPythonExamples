"""Inverse Kinematik eines planaren Roboters mit zwei Drehgelenken."""

import math


ARM_1_MM = 100.0
ARM_2_MM = 80.0


def inverse_kinematik(x: float, y: float) -> tuple[float, float] | None:
    """Gib (alpha, beta) in Grad zurück, bei unerreichbaren Zielen None."""
    if not math.isfinite(x) or not math.isfinite(y):
        return None

    abstand = math.hypot(x, y)
    if not abs(ARM_1_MM - ARM_2_MM) <= abstand <= ARM_1_MM + ARM_2_MM:
        return None

    cos_beta = (
        x * x + y * y - ARM_1_MM**2 - ARM_2_MM**2
    ) / (2 * ARM_1_MM * ARM_2_MM)
    # Rundungsfehler an den Grenzen dürfen acos nicht aus [-1, 1] führen.
    cos_beta = max(-1.0, min(1.0, cos_beta))
    beta_rad = math.acos(cos_beta)

    alpha_rad = math.atan2(y, x) - math.atan2(
        ARM_2_MM * math.sin(beta_rad),
        ARM_1_MM + ARM_2_MM * math.cos(beta_rad),
    )
    return math.degrees(alpha_rad), math.degrees(beta_rad)


if __name__ == "__main__":
    x, y = 100.0, 80.0
    winkel = inverse_kinematik(x, y)
    print(f"Zielposition: x = {x:.2f} mm, y = {y:.2f} mm")
    if winkel is None:
        print("Der Zielpunkt ist nicht erreichbar.")
    else:
        alpha, beta = winkel
        print(f"alpha = {alpha:.2f}°, beta = {beta:.2f}°")
