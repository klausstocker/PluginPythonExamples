"""Energiekosten mit Standardtarif."""

def energiekosten(energie_kwh: float, preis_pro_kwh: float = 0.30) -> float:
    return energie_kwh * preis_pro_kwh


if __name__ == "__main__":
    print(energiekosten(4.0))
    print(energiekosten(4.0, 0.25))
