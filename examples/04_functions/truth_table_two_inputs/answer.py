"""Alle 16 Varianten: Ausgangsbits in der Reihenfolge 00, 01, 10, 11."""


def funktion_0(a: bool, b: bool) -> bool:
    return False


def funktion_1(a: bool, b: bool) -> bool:
    return a and b


def funktion_2(a: bool, b: bool) -> bool:
    return a and not b


def funktion_3(a: bool, b: bool) -> bool:
    return a


def funktion_4(a: bool, b: bool) -> bool:
    return not a and b


def funktion_5(a: bool, b: bool) -> bool:
    return b


def funktion_6(a: bool, b: bool) -> bool:
    return (a and not b) or (not a and b)


def funktion_7(a: bool, b: bool) -> bool:
    return a or b


def funktion_8(a: bool, b: bool) -> bool:
    return not (a or b)


def funktion_9(a: bool, b: bool) -> bool:
    return (a and b) or (not a and not b)


def funktion_10(a: bool, b: bool) -> bool:
    return not b


def funktion_11(a: bool, b: bool) -> bool:
    return a or not b


def funktion_12(a: bool, b: bool) -> bool:
    return not a


def funktion_13(a: bool, b: bool) -> bool:
    return not a or b


def funktion_14(a: bool, b: bool) -> bool:
    return not (a and b)


def funktion_15(a: bool, b: bool) -> bool:
    return True


if __name__ == "__main__":
    funktionen = [
        funktion_0, funktion_1, funktion_2, funktion_3,
        funktion_4, funktion_5, funktion_6, funktion_7,
        funktion_8, funktion_9, funktion_10, funktion_11,
        funktion_12, funktion_13, funktion_14, funktion_15,
    ]
    print("Variante  Ausgänge für 00, 01, 10, 11")
    for variante, funktion in enumerate(funktionen):
        ausgaenge = ""
        for a, b in [(False, False), (False, True), (True, False), (True, True)]:
            ausgaenge += str(int(funktion(a, b)))
        print(f"{variante:>8}  {ausgaenge}")
