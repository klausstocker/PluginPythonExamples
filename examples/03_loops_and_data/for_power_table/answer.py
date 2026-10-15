"""Für jeden Stromwert die Leistungsfunktion aufrufen."""

import dataset


def leistung_watt(spannung: float, strom: float) -> float:
    return spannung * strom


spannung = float(dataset.spannung.value)
start = int(dataset.start.value)
stopp = int(dataset.stopp.value)
schrittweite = int(dataset.schrittweite.value)

for strom in range(start, stopp, schrittweite):
    leistung = leistung_watt(spannung, strom)
    print(f"I = {strom} A: {leistung:.1f} W")
