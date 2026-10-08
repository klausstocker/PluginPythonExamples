# Die 16 logischen Funktionen mit zwei Eingängen

## Lernziel

Wahrheitstabellen als Binärzahlen nummerieren und daraus Python-Funktionen
mit `and`, `or` und `not` ableiten.

## Aufgabe

Zwei boolesche Eingänge besitzen vier Kombinationen. Verwende immer die
Zeilenfolge **00, 01, 10, 11** für `(a, b)`. Lies die vier Ausgangswerte von
oben nach unten als Binärzahl: Der Ausgang für `00` ist das höchstwertige Bit,
der Ausgang für `11` das niedrigstwertige Bit.
Damit gibt es `2 ** 4 = 16` verschiedene Wahrheitstabellen.
`0` bedeutet `False`, `1` bedeutet `True`.

| Variante | Ausgangsbits | y für 00 | y für 01 | y für 10 | y für 11 |
| --- | --- | --- | --- | --- | --- |
| 0 | 0000 | 0 | 0 | 0 | 0 |
| 1 | 0001 | 0 | 0 | 0 | 1 |
| 2 | 0010 | 0 | 0 | 1 | 0 |
| 3 | 0011 | 0 | 0 | 1 | 1 |
| 4 | 0100 | 0 | 1 | 0 | 0 |
| 5 | 0101 | 0 | 1 | 0 | 1 |
| 6 | 0110 | 0 | 1 | 1 | 0 |
| 7 | 0111 | 0 | 1 | 1 | 1 |
| 8 | 1000 | 1 | 0 | 0 | 0 |
| 9 | 1001 | 1 | 0 | 0 | 1 |
| 10 | 1010 | 1 | 0 | 1 | 0 |
| 11 | 1011 | 1 | 0 | 1 | 1 |
| 12 | 1100 | 1 | 1 | 0 | 0 |
| 13 | 1101 | 1 | 1 | 0 | 1 |
| 14 | 1110 | 1 | 1 | 1 | 0 |
| 15 | 1111 | 1 | 1 | 1 | 1 |

Schreibe für jede Variante eine eigene Funktion `funktion_0` bis `funktion_15`
mit zwei booleschen Parametern und booleschem Rückgabewert, zum Beispiel:

```python
def funktion_6(a: bool, b: bool) -> bool:
    ...
```

Verwende die Eingänge, `and`, `or`, `not`, Klammern und bei Bedarf die Konstanten
`True` und `False`. Keine `if`-Anweisungen, Nachschlagetabellen, Vergleiche oder
bitweisen Operatoren. Die Funktionen geben nur den booleschen Wert mit `return`
zurück und erzeugen keine Ausgabe.

Beispiel: Variante 6 hat die Ausgangsbits `0110`. Daher liefert
`funktion_6(False, True)` den Wert `True` und `funktion_6(True, True)` den Wert `False`.

## Dateien

- `answer.py` enthält alle 16 Musterlösungen und eine Demonstration ihrer Ausgangsbits.
- `test_answer.py` vergleicht alle 64 Rückgabewerte mit `correct()`.

## Voraussetzungen

Python 3, nur Standardbibliothek. Kenntnisse zu `bool`, logischen Operatoren,
Funktionen und Binärzahlen. Alle Argumente sind boolesche Werte.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/04_functions/truth_table_two_inputs/answer.py
python -m unittest discover -s examples/04_functions/truth_table_two_inputs -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Beginne mit den Zeilen, deren Ausgang 1 ist. Beschreibe jede Kombination mit
UND und negierten Eingängen und verbinde diese Terme mit ODER. Anschließend
können Terme vereinfacht werden.

Bekannte Varianten sind UND (1), XOR (6), ODER (7), NOR (8), XNOR (9) und NAND (14).
Variante 13 beschreibt die Implikation von `a` nach `b`. Die Nummerierung hängt
von der oben festgelegten Reihenfolge der Ausgangsbits ab.

Die Referenzfunktion liest die Bits der Variantennummer unabhängig von der
Musterlösung. Der Test prüft alle Kombinationen und verlangt echte boolesche
Rückgabewerte. Die verwendeten Operatoren werden beim Lesen des Schülercodes geprüft.
