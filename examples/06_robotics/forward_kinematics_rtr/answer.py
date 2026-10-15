"""Vorwärtskinematik des planaren RTR-Roboters aus dem Robotik-Skript."""

import math


TCP_OFFSET_MM = 0.9
MAX_EXTENSION_MM = 7.0


def forward_kinematics(
    r1: float, d: float, r2: float
) -> tuple[float, float, float] | None:
    """Gib (x, y, phi) in mm und Grad zurück, bei ungültigen Werten None."""
    if not all(math.isfinite(value) for value in (r1, d, r2)):
        return None
    if not 0.0 <= d <= MAX_EXTENSION_MM:
        return None

    phi = r1 + r2
    base_angle_rad = math.radians(r1)
    gripper_angle_rad = math.radians(phi)

    wrist_x = d * math.cos(base_angle_rad)
    wrist_y = d * math.sin(base_angle_rad)
    # Der TCP liegt entlang der lokalen positiven y-Achse des Greifers.
    x = wrist_x - TCP_OFFSET_MM * math.sin(gripper_angle_rad)
    y = wrist_y + TCP_OFFSET_MM * math.cos(gripper_angle_rad)
    return x, y, phi


if __name__ == "__main__":
    pose = forward_kinematics(31.476839350, 5.745432969, 58.523160650)
    if pose is not None:
        x, y, phi = pose
        print(f"TCP: x = {x:.3f} mm, y = {y:.3f} mm")
        print(f"Greiferorientierung: phi = {phi:.3f}°")
