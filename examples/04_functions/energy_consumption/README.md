# Energieverbrauch berechnen

## Lernziel

Parameter und Rückgabewert mit Type Hints dokumentieren; Einheiten umrechnen.

## Aufgabe

Schreibe `energie_kwh(leistung_watt: float, dauer_stunden: float) -> float`. Gib den Energieverbrauch in kWh zurück: Leistung in W mal Dauer in Stunden geteilt durch 1000.

## Dateien

- `answer.py` enthält die Musterlösung und eine Demonstration.
- `test_answer.py` prüft die Ergebnisse mit anderen Eingaben und Grenzfällen.

## Voraussetzungen

Python 3, nur Standardbibliothek. Variablen und Grundrechenarten. Konstante Leistung; Leistung und Dauer sind nichtnegative Zahlen. Alle Funktionsaufrufe verwenden Positionsargumente; benannte Argumente sind nicht erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/04_functions/energy_consumption/answer.py
python -m unittest discover -s examples/04_functions/energy_consumption -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Die Funktion liefert einen Zahlenwert, keine Ausgabe. Type Hints dokumentieren Typen und führen keine automatische Umwandlung aus.
