"""Den Ostersonntag mit der gregorianischen Osterformel von Gauß berechnen."""

from datetime import date, timedelta


def ostersonntag(jahr: int) -> date:
    """Gib den westlichen Ostersonntag für ein Jahr von 1583 bis 4099 zurück."""
    if not 1583 <= jahr <= 4099:
        raise ValueError("Das Jahr muss zwischen 1583 und 4099 liegen.")

    # Die Reste beschreiben die Position im Mond- und Sonnenzyklus.
    mondzyklus = jahr % 19
    schaltjahr_rest = jahr % 4
    wochen_rest = jahr % 7
    jahrhundert = jahr // 100

    mondkorrektur = (13 + 8 * jahrhundert) // 25
    schaltkorrektur = jahrhundert // 4
    mond_offset = (15 - mondkorrektur + jahrhundert - schaltkorrektur) % 30
    wochen_offset = (4 + jahrhundert - schaltkorrektur) % 7

    vollmond_rest = (19 * mondzyklus + mond_offset) % 30
    sonntag_rest = (
        2 * schaltjahr_rest + 4 * wochen_rest + 6 * vollmond_rest + wochen_offset
    ) % 7

    # Zwei Sonderfälle korrigieren einen sonst um eine Woche zu späten Termin.
    if vollmond_rest == 29 and sonntag_rest == 6:
        sonntag_rest -= 7
    elif vollmond_rest == 28 and sonntag_rest == 6 and mondzyklus > 10:
        sonntag_rest -= 7

    return date(jahr, 3, 22) + timedelta(days=vollmond_rest + sonntag_rest)


if __name__ == "__main__":
    print(ostersonntag(2026).strftime("%d.%m.%Y"))
