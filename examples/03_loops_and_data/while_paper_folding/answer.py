"""Eine Dicke durch wiederholte Funktionsaufrufe verdoppeln."""

import dataset


def doppelte_dicke(dicke: float) -> float:
    return dicke * 2

dicke = float(dataset.dicke.value)
ziel = float(dataset.ziel.value)
faltungen = 0

while dicke < ziel:
    dicke = doppelte_dicke(dicke)
    faltungen = faltungen + 1

print(f'Faltungen: {faltungen}')
print(f'Dicke: {dicke:.3f} mm')
