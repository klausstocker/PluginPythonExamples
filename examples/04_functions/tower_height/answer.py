"""Die Höhe eines Turms mit dem Tangens berechnen."""

import math


def turmhoehe(
    abstand_m: float, winkel_grad: float, messhoehe_m: float = 1.5
) -> float:
    """Berechne die Turmhöhe in Metern bei waagerechtem Gelände."""
    winkel_rad = math.radians(winkel_grad)
    hoehenunterschied_m = abstand_m * math.tan(winkel_rad)
    return hoehenunterschied_m + messhoehe_m


if __name__ == "__main__":
    hoehe_m = turmhoehe(20.0, 35.0)
    print(f"Turmhöhe bei Standardmesshöhe: {hoehe_m:.2f} m")

    hoehe_m = turmhoehe(30.0, 40.0, 1.7)
    print(f"Turmhöhe bei 1,70 m Messhöhe: {hoehe_m:.2f} m")
