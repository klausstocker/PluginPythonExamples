"""Bestellungen mit Dataclasses beschreiben und prüfen."""

from dataclasses import dataclass


@dataclass
class Artikel:
    name: str
    bestand: int
    aktiv: bool


@dataclass
class Bestellung:
    kunde: str
    menge: int


@dataclass
class Bestellergebnis:
    kunde: str
    artikel: str
    menge: int
    lieferbar: bool


def bestellung_pruefen(
    artikel: Artikel, bestellung: Bestellung
) -> Bestellergebnis:
    """Erstelle ein neues Ergebnisobjekt aus Artikel- und Bestelldaten."""
    lieferbar = artikel.aktiv and bestellung.menge <= artikel.bestand
    ergebnis = Bestellergebnis(
        kunde=bestellung.kunde,
        artikel=artikel.name,
        menge=bestellung.menge,
        lieferbar=lieferbar,
    )
    return ergebnis


if __name__ == "__main__":
    artikel = Artikel("Bleistift", 20, True)
    bestellung = Bestellung("Mia", 5)
    ergebnis = bestellung_pruefen(artikel, bestellung)
    print(ergebnis)
    print(f"Lieferbar: {ergebnis.lieferbar}")
