"""Beide Grenzwerte erreicht: Messwerte logisch verknüpfen."""


def pruefe_messwerte(temperatur, strom):
    """Beide Grenzwerte erreicht: True oder False zurückgeben."""
    temperatur_auffaellig = temperatur >= 60
    strom_auffaellig = strom >= 10
    return temperatur_auffaellig and strom_auffaellig


if __name__ == "__main__":
    print(pruefe_messwerte(70, 11))
