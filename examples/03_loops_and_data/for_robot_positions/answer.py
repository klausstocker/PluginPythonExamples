"""Positionen nach gleich großen Verfahrwegen berechnen."""

import dataset

anzahl = int(dataset.anzahl.value)
schrittweite = float(dataset.schrittweite.value)

for schritt in range(1, anzahl + 1):
    position = schritt * schrittweite
    print(f"Schritt {schritt}: {position:.1f} mm")
