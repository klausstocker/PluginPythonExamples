"""Energieverbrauch berechnen."""

def energie_kwh(leistung_watt: float, dauer_stunden: float) -> float:
    energie = leistung_watt * dauer_stunden / 1000.0
    return energie


if __name__ == "__main__":
    print(energie_kwh(1500.0, 2.0))
    print(energie_kwh(80.0, 5.0))
