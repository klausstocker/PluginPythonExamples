"""Die Dauer einer festgelegten Versuchsreihe aufsummieren."""

import dataset

anzahl = int(dataset.anzahl.value)
startdauer = float(dataset.startdauer.value)
zuwachs = float(dataset.zuwachs.value)

gesamtdauer = 0.0
dauer = startdauer

for versuch in range(anzahl):
    gesamtdauer = gesamtdauer + dauer
    dauer = dauer + zuwachs

print(f"Gesamtdauer: {gesamtdauer:.1f} s")
