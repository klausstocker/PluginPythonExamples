"""Die Ziffern einer Teilenummer von rechts nach links addieren."""

import dataset

teilenummer = int(dataset.teilenummer.value)
rest = teilenummer
quersumme = 0

while rest > 0:
    letzte_ziffer = rest % 10
    quersumme = quersumme + letzte_ziffer
    rest = rest // 10

print(f'Quersumme: {quersumme}')
