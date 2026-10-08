"""Primzahlen mit einer Hilfsfunktion prüfen und in einem Bereich sammeln."""


def ist_primzahl(zahl: int) -> bool:
    """Prüfe, ob die Zahl genau zwei positive Teiler besitzt."""
    if zahl < 2:
        return False

    teiler = 2
    while teiler * teiler <= zahl:
        if zahl % teiler == 0:
            return False
        teiler += 1
    return True


def primzahlen_im_bereich(start: int, ende: int) -> list[int]:
    """Gib alle Primzahlen von start bis ende einschließlich zurück."""
    primzahlen = []
    for zahl in range(start, ende + 1):
        if ist_primzahl(zahl):
            primzahlen.append(zahl)
    return primzahlen


if __name__ == "__main__":
    print(primzahlen_im_bereich(10, 30))
