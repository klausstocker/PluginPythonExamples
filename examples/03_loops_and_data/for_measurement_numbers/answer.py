"""Eine vorgegebene Anzahl von Messungen nummerieren."""

import dataset

anzahl = int(dataset.a.value)

for index in range(anzahl):
    print(f"Messung {index + 1}")
print("Fertig.")
