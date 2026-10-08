# Pascalsches Dreieck ausgeben

## Lernziel

Eine Funktion mit einem Parameter und dem Rückgabetyp `str` schreiben.
Mit Listen und Schleifen aufeinanderfolgende Zeilen berechnen und einen String
aufbauen. Den Rückgabewert außerhalb der Funktion auf stdout ausgeben.

## Aufgabe

Schreibe die Funktion `pascalsches_dreieck(anzahl_zeilen: int) -> str`.
Sie soll die angegebene Anzahl Zeilen des pascalschen Dreiecks als String
zurückgeben. Gib diesen String außerhalb der Funktion mit
`print(pascalsches_dreieck(5), end="")` auf stdout (im Terminal) aus.

- Die erste Zeile enthält nur die Zahl `1`.
- Jede weitere Zeile beginnt und endet mit `1`.
- Jede Zahl dazwischen ist die Summe der beiden benachbarten Zahlen der vorherigen Zeile.
- Gib jede Zeile linksbündig aus. Trenne die Zahlen durch genau ein Leerzeichen;
  verwende keine Leerzeichen am Zeilenanfang oder -ende.
- Beende jede ausgegebene Zeile mit einem Zeilenumbruch. Gib keine Überschrift
  und keine zusätzlichen Leerzeilen aus.
- Bei `anzahl_zeilen = 0` gibt die Funktion den leeren String `""` zurück.
  Innerhalb der Funktion wird kein `print()` verwendet.

Beispiel für `pascalsches_dreieck(5)`:

```text
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

## Dateien

- `answer.py` enthält die Musterlösung und einen Beispielaufruf.
- `test_answer.py` vergleicht die Rückgabewerte direkt mit der Referenzfunktion
  `correct()` und prüft wiederholte Aufrufe.

## Voraussetzungen

Python 3.8 oder neuer, nur Standardbibliothek. Kenntnisse zu Listen, Schleifen,
`str()` und `join()`. Die Anzahl der Zeilen ist eine nichtnegative ganze Zahl;
eine Eingabeprüfung ist nicht Teil der Aufgabe.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/04_functions/pascal_triangle/answer.py
python -m unittest discover -s examples/04_functions/pascal_triangle -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Die Musterlösung baut jede neue Zeile aus der vorherigen auf. Eine separate
Liste verhindert, dass während der Berechnung benötigte Werte überschrieben werden.
Jeder Funktionsaufruf beginnt wieder mit `[1]`.

Die Funktion liefert mit `return` einen String; die aufrufende Stelle übernimmt
die Ausgabe mit `print()`. `end=""` verhindert einen zusätzlichen Zeilenumbruch.
Die Tests vergleichen ausschließlich die Rückgabewerte einschließlich
Leerzeichen und Zeilenumbrüchen. `correct()` nutzt `math.comb()` zur
unabhängigen Berechnung; Binomialkoeffizienten müssen für die Schülerlösung
nicht bekannt sein.
