"""Kein Grenzwert erreicht: Messwerte logisch verknüpfen."""


def pruefe_messwerte(temperatur, strom):
    """Kein Grenzwert erreicht: True oder False zurückgeben."""
    temperatur_auffaellig = temperatur >= 60
    strom_auffaellig = strom >= 10
    return not (temperatur_auffaellig or strom_auffaellig)


if __name__ == "__main__":
    print(pruefe_messwerte(70, 11))
