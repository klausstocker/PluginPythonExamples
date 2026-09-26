"""Den Winkel zwischen zwei Richtungsvektoren mit NumPy berechnen."""

import numpy as np
from numpy.typing import NDArray


def winkel_zwischen_vektoren(
    vektor_a: NDArray[np.float64], vektor_b: NDArray[np.float64]
) -> float:
    """Winkel in Grad (0 bis 180) für zwei Arrays der Form (3,) berechnen.

    Falsche Formen, nicht endliche Werte und Nullvektoren führen zu ValueError.
    """
    if vektor_a.shape != (3,) or vektor_b.shape != (3,):
        raise ValueError("Jeder Vektor muss genau drei Komponenten haben.")
    if not np.all(np.isfinite(vektor_a)) or not np.all(np.isfinite(vektor_b)):
        raise ValueError("Die Komponenten müssen endlich sein.")

    laenge_a = np.linalg.norm(vektor_a)
    laenge_b = np.linalg.norm(vektor_b)
    if laenge_a == 0 or laenge_b == 0:
        raise ValueError("Für Nullvektoren ist kein Winkel definiert.")

    skalarprodukt = np.dot(vektor_a, vektor_b)
    kosinus = skalarprodukt / (laenge_a * laenge_b)
    # Rundungsfehler dürfen den Definitionsbereich von arccos nicht verlassen.
    kosinus = np.clip(kosinus, -1.0, 1.0)
    winkel_radiant = np.arccos(kosinus)
    return float(np.degrees(winkel_radiant))


if __name__ == "__main__":
    richtung_a = np.array([3.0, 1.0, 1.0], dtype=np.float64)
    richtung_b = np.array([1.0, 3.0, 2.0], dtype=np.float64)
    winkel = winkel_zwischen_vektoren(richtung_a, richtung_b)
    print(f"Winkel: {winkel:.2f} Grad")
