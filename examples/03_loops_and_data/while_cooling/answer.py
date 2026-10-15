"""Mit einer Zustandsfunktion eine Zieltemperatur erreichen."""

import dataset


def abkuehlen(temperatur: float, umgebung: float) -> float:
    return (temperatur + umgebung) / 2

temperatur = float(dataset.temperatur.value)
umgebung = float(dataset.umgebung.value)
ziel = float(dataset.ziel.value)
schritte = 0

while temperatur > ziel:
    temperatur = abkuehlen(temperatur, umgebung)
    schritte = schritte + 1

print(f'Schritte: {schritte}')
print(f'Temperatur: {temperatur:.2f} °C')
