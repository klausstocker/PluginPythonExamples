"""Vom Energieverbrauch zu den Kosten."""

def energie_kwh(leistung_watt: float, dauer_stunden: float) -> float:
    return leistung_watt * dauer_stunden / 1000.0


def energiekosten(energie_kwh: float, preis_pro_kwh: float = 0.30) -> float:
    return energie_kwh * preis_pro_kwh


def betriebskosten(leistung_watt: float, dauer_stunden: float, preis_pro_kwh: float = 0.30) -> float:
    verbrauch = energie_kwh(leistung_watt, dauer_stunden)
    kosten = energiekosten(verbrauch, preis_pro_kwh)
    return kosten


if __name__ == "__main__":
    print(betriebskosten(1500.0, 2.0))
    print(betriebskosten(1500.0, 2.0, 0.25))
