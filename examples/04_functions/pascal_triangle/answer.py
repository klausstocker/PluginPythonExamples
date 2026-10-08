"""Das pascalsche Dreieck als String berechnen und auf stdout ausgeben."""


def pascalsches_dreieck(anzahl_zeilen: int) -> str:
    """Gib die gewünschte Anzahl Zeilen als String zurück."""
    ausgabe = ""
    zeile = [1]
    for _ in range(anzahl_zeilen):
        zahlen = []
        for zahl in zeile:
            zahlen.append(str(zahl))
        ausgabe += " ".join(zahlen) + "\n"

        naechste_zeile = [1]
        for index in range(len(zeile) - 1):
            naechste_zeile.append(zeile[index] + zeile[index + 1])
        naechste_zeile.append(1)
        zeile = naechste_zeile
    return ausgabe


if __name__ == "__main__":
    print(pascalsches_dreieck(5), end="")
