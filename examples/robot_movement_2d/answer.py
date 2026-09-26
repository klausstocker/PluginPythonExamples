"""Reference solutions for constant-velocity movements in two dimensions."""

import numpy as np
from numpy.typing import NDArray


def end_position(
    start_point: NDArray[np.float64],
    velocity: NDArray[np.float64],
    delta_t: float,
) -> NDArray[np.float64]:
    """Return the position after delta_t seconds at a constant velocity."""
    return start_point + velocity * delta_t


def end_position_after_movements(
    start_point: NDArray[np.float64],
    movements: list[tuple[float, float, float]],
) -> NDArray[np.float64]:
    """Follow (angle_degrees, speed, delta_t) movements in a fixed frame."""
    position = start_point.copy()

    for angle_degrees, speed, delta_t in movements:
        angle_radians = np.deg2rad(angle_degrees)
        velocity = speed * np.array([
            np.cos(angle_radians),
            np.sin(angle_radians),
        ])
        position = end_position(position, velocity, delta_t)

    return position


if __name__ == "__main__":
    start = np.array([1.0, 2.0])
    velocity = np.array([0.5, -1.0])
    print("After one movement:", end_position(start, velocity, 4.0))

    movements = [(0.0, 2.0, 3.0), (90.0, 1.0, 2.0)]
    print("After all movements:", end_position_after_movements(start, movements))
