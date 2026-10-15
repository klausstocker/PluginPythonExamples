"""Inverse Kinematik des planaren RTR-Roboters mit TCP-Versatz."""

import math


TCP_OFFSET_MM = 0.9
MAX_EXTENSION_MM = 7.0
LENGTH_TOLERANCE_MM = 1e-12


def inverse_kinematics(
    x: float, y: float, phi: float
) -> tuple[float, float, float] | None:
    """Gib (r1, d, r2) in Grad, mm, Grad zurück, bei unerreichbaren Posen None."""
    if not all(math.isfinite(value) for value in (x, y, phi)):
        return None

    gripper_angle_rad = math.radians(phi)
    # Den gedrehten TCP-Versatz abziehen, um das Handgelenk zu erhalten.
    wrist_x = x + TCP_OFFSET_MM * math.sin(gripper_angle_rad)
    wrist_y = y - TCP_OFFSET_MM * math.cos(gripper_angle_rad)
    d = math.hypot(wrist_x, wrist_y)
    if d > MAX_EXTENSION_MM:
        if not math.isclose(d, MAX_EXTENSION_MM, rel_tol=0.0, abs_tol=LENGTH_TOLERANCE_MM):
            return None
        d = MAX_EXTENSION_MM

    if d <= LENGTH_TOLERANCE_MM:
        # Im Ursprung ist die Armrichtung frei wählbar; wir wählen r1 = 0°.
        r1 = 0.0
        d = 0.0
    else:
        r1 = math.degrees(math.atan2(wrist_y, wrist_x))
    r2 = phi - r1
    return r1, d, r2


if __name__ == "__main__":
    joints = inverse_kinematics(4.0, 3.0, 90.0)
    if joints is None:
        print("Die Zielpose ist nicht erreichbar.")
    else:
        r1, d, r2 = joints
        print(f"r1 = {r1:.6f}°, d = {d:.6f} mm, r2 = {r2:.6f}°")
