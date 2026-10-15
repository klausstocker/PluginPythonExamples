"""Einen Füllstand erhöhen, bis das Ziel erreicht ist."""

import dataset

fuellstand = float(dataset.fuellstand.value)
ziel = float(dataset.ziel.value)
zufluss = float(dataset.zufluss.value)
schritte = 0

while fuellstand < ziel:
    fuellstand = fuellstand + zufluss
    schritte = schritte + 1

print(f'Schritte: {schritte}')
print(f'Füllstand: {fuellstand:.1f} l')
