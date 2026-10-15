"""Vorwärtskinematik eines planaren Roboters mit zwei Drehgelenken."""

import math


ARM_1_MM = 100.0
ARM_2_MM = 80.0


def forward_kinematics(alpha: float, beta: float) -> tuple[float, float] | None:
    """Gib die Endpunktposition (x, y) in mm zurück, bei ungültigen Winkeln None."""
    if not math.isfinite(alpha) or not math.isfinite(beta):
        return None

    first_angle_rad = math.radians(alpha)
    second_angle_rad = math.radians(alpha + beta)
    x = ARM_1_MM * math.cos(first_angle_rad) + ARM_2_MM * math.cos(second_angle_rad)
    y = ARM_1_MM * math.sin(first_angle_rad) + ARM_2_MM * math.sin(second_angle_rad)
    return x, y


if __name__ == "__main__":
    position = forward_kinematics(0.0, 90.0)
    if position is not None:
        x, y = position
        print(f"Endpunkt: x = {x:.3f} mm, y = {y:.3f} mm")
