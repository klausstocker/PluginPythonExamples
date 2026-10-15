"""Vollständige Kartons durch wiederholtes Abziehen zählen."""

import dataset

bestand = int(dataset.bestand.value)
kartongroesse = int(dataset.kartongroesse.value)
kartons = 0

while bestand >= kartongroesse:
    bestand = bestand - kartongroesse
    kartons = kartons + 1

print(f'Kartons: {kartons}')
print(f'Rest: {bestand}')
