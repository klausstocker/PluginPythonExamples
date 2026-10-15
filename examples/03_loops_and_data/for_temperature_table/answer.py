"""Eine Umrechnungsfunktion für alle Tabellenzeilen verwenden."""

import dataset


def fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


start = int(dataset.start.value)
stopp = int(dataset.stopp.value)
schrittweite = int(dataset.schrittweite.value)

for celsius in range(start, stopp, schrittweite):
    temperatur_fahrenheit = fahrenheit(celsius)
    print(f"{celsius} °C = {temperatur_fahrenheit:.1f} °F")
