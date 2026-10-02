"""Spannungsbereich als Funktion."""

def spannung_im_bereich(spannung: float, minimum: float = 210.0, maximum: float = 250.0) -> bool:
    return spannung >= minimum and spannung <= maximum


if __name__ == "__main__":
    print(spannung_im_bereich(230.0))
    print(spannung_im_bereich(215.0, 220.0))
    print(spannung_im_bereich(24.0, 22.0, 26.0))
