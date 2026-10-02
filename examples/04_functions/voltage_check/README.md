# Spannungsbereich als Funktion

## Lernziel

Eine Funktion mit booleschem Rückgabewert und Standardgrenzen schreiben.

## Aufgabe

Schreibe `spannung_im_bereich(spannung: float, minimum: float = 210.0, maximum: float = 250.0) -> bool`. Beide Grenzen gehören zum erlaubten Bereich. Gib das Ergebnis der Vergleiche direkt zurück. Verwende Aufrufe mit einer, zwei und drei Positionsangaben.

## Dateien

- `answer.py` enthält die Musterlösung und eine Demonstration.
- `test_answer.py` prüft die Ergebnisse mit anderen Eingaben und Grenzfällen.

## Voraussetzungen

Python 3, nur Standardbibliothek. Variablen und Grundrechenarten. Spannungen in V; minimum <= maximum. Die Grenzen sind Übungsvorgaben. Alle Funktionsaufrufe verwenden Positionsargumente; benannte Argumente sind nicht erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/04_functions/voltage_check/answer.py
python -m unittest discover -s examples/04_functions/voltage_check -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Dieses Beispiel greift das Boolean-Beispiel voltage_range auf. Die Reihenfolge der Positionsargumente ist entscheidend.
