# Primzahlen in einem Bereich finden

## Lernziel

Eine Aufgabe auf zwei Funktionen aufteilen: Eine Hilfsfunktion prüft eine einzelne
Zahl, die andere sammelt passende Zahlen in einer Liste. Boolesche Rückgabewerte,
Schleifen, Teilbarkeit mit `%` und `append()` verwenden.

## Aufgabe

Schreibe diese beiden Funktionen:

```python
def ist_primzahl(zahl: int) -> bool:
    ...

def primzahlen_im_bereich(start: int, ende: int) -> list[int]:
    ...
```

Eine **Primzahl** ist eine ganze Zahl größer als 1, die nur durch 1 und sich selbst
ohne Rest teilbar ist.

1. `ist_primzahl()` gibt `True` zurück, wenn die Zahl eine Primzahl ist, sonst
   `False`. Zahlen kleiner als 2 sind keine Primzahlen.
2. `primzahlen_im_bereich()` verwendet diese Hilfsfunktion und gibt alle Primzahlen
   von `start` bis `ende` **einschließlich beider Grenzen** als aufsteigend sortierte
   Liste zurück.
3. Enthält der Bereich keine Primzahlen oder gilt `start > ende`, gib `[]` zurück.
4. Gib das Ergebnis außerhalb der Funktionen mit `print()` aus.

Beispiel:

```python
primzahlen_im_bereich(10, 30)
# Rückgabewert: [11, 13, 17, 19, 23, 29]
```

## Dateien

- `answer.py` enthält beide Funktionen und einen Beispielaufruf.
- `test_answer.py` vergleicht die Rückgabewerte mit Referenzfunktionen.
  `correct()` liefert die erwartete Liste.

## Voraussetzungen

Python 3.9 oder neuer, nur Standardbibliothek. Kenntnisse zu Funktionen,
`if`, Schleifen, Listen und `%`. Die Argumente sind ganze Zahlen;
eine Prüfung der Datentypen ist nicht Teil der Aufgabe.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/04_functions/prime_numbers/answer.py
python -m unittest discover -s examples/04_functions/prime_numbers -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Die Hilfsfunktion ist eine separate Funktion auf Modulebene, die von
`primzahlen_im_bereich()` aufgerufen wird. Die Tests vergleichen ausschließlich
Rückgabewerte. Ob die Hilfsfunktion tatsächlich verwendet wird, lässt sich im Code prüfen.

Zum Einstieg können alle Teiler von 2 bis `zahl - 1` geprüft werden, wie in der
Referenzfunktion der Tests. Die Musterlösung prüft nur so lange,
wie `teiler * teiler <= zahl` gilt: Bei einem Teilerpaar liegt mindestens ein
Teiler höchstens bei der Quadratwurzel. Das Gleichheitszeichen ist wichtig,
damit auch Quadratzahlen wie 49 als zusammengesetzt erkannt werden.
Die Rechnung mit ganzen Zahlen benötigt weder `math` noch Rundungen.
