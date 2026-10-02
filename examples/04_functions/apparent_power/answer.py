"""Scheinleistung als Funktion."""

import math


def scheinleistung(wirkleistung, blindleistung):
    scheinleistung_va = math.sqrt(wirkleistung ** 2 + blindleistung ** 2)
    return scheinleistung_va


if __name__ == "__main__":
    print(scheinleistung(800.0, 600.0))
    print(scheinleistung(2000.0, 0.0))
