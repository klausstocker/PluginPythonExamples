# Personen aus einer Liste von Tupeln filtern

## Lernziel

Die Lernenden durchlaufen eine Liste mit einer `for`-Schleife, entpacken Tupel
und verwenden Vergleiche, `len`, den Modulo-Operator `%` und das logische `or`.
Die Ausgabe erfolgt mit `print` auf stdout.

## Aufgabe

Gegeben ist eine Liste von Tupeln `(name: str, alter: int)`:

```python
people = [("Anna", 8), ("Benjamin", 11), ("Clara", 10), ("David", 9)]
```

Implementiere zwei voneinander unabhängige Filter:

1. `print_names_under_ten(people)` gibt nur die Namen der Personen aus,
   deren Alter **kleiner als 10** ist.
2. `print_names_long_or_even_age(people)` gibt nur die Namen der Personen aus,
   deren Name **mehr als 5 Buchstaben** hat **oder** deren Alter **durch 2
   teilbar** ist. Es genügt, wenn eine der beiden Bedingungen erfüllt ist.

Gib jeden passenden Namen auf einer eigenen Zeile aus. Behalte die Reihenfolge
der Liste bei. Gib keine Altersangaben, Überschriften oder Listenklammern aus.
Wenn beide Bedingungen des zweiten Filters erfüllt sind, erscheint der Name
trotzdem nur einmal für diesen Listeneintrag. Die Funktionen geben keine
Ergebnisliste zurück.

Ausgabe für Aufgabe 1:

```text
Anna
David
```

Ausgabe für Aufgabe 2:

```text
Anna
Benjamin
Clara
```

## Dateien

- `answer.py`: Referenzlösung und Beispieldaten; beim direkten Start werden
  beide Aufgaben nacheinander ausgeführt.
- `test_answer.py`: `unittest`-Tests mit anderen Personen, Grenzwerten,
  allen Kombinationen der Oder-Bedingung und leeren Ergebnissen.

## Ausführen und testen

Voraussetzung: Python 3.9 oder neuer. Keine externen Abhängigkeiten.
Die Namen bestehen ausschließlich aus Buchstaben; daher entspricht `len(name)`
hier der Anzahl der Buchstaben. Die Alterswerte sind nichtnegative Ganzzahlen.

Aus dem Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

Aus dem Repository-Stammverzeichnis:

```bash
python -m unittest discover -s examples/03_loops_and_data/filter_people -p "test_*.py"
```

## Hinweise für Lehrkräfte

Die Aufgaben können getrennt bearbeitet werden. Ersetze für eigene Übungen die
Personenliste. Besprich die Grenzen `age == 10` und `len(name) == 5`, die beide
die jeweilige strenge Vergleichsbedingung nicht erfüllen. Bei Aufgabe 2 kann
ein Name mit genau fünf Buchstaben dennoch wegen eines geraden Alters erscheinen.
