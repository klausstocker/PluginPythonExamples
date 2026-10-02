# 4. Funktionen

Fünf selbstständige Beispiele passend zum Kapitel Funktionen im Informatikskript.
Die Reihenfolge führt von `def` und `return` über Type Hints und Standardwerte
zum Kombinieren von Funktionen. Alle Aufrufe verwenden Positionsargumente.

## Empfohlene Reihenfolge

1. [Scheinleistung als Funktion](apparent_power/README.md): Eine Funktion definieren, mit mehreren Argumenten aufrufen und einen lokalen Ergebniswert zurückgeben.
2. [Energieverbrauch berechnen](energy_consumption/README.md): Parameter und Rückgabewert mit Type Hints dokumentieren; Einheiten umrechnen.
3. [Energiekosten mit Standardtarif](energy_cost/README.md): Einen unveränderlichen Standardwert für einen Parameter verwenden.
4. [Spannungsbereich als Funktion](voltage_check/README.md): Eine Funktion mit booleschem Rückgabewert und Standardgrenzen schreiben.
5. [Vom Energieverbrauch zu den Kosten](consumption_to_cost/README.md): Den Rückgabewert einer Funktion an eine andere Funktion weitergeben.

## Tests

Jedes Beispiel enthält seine Testbefehle im README. Alle Beispiele:

```bash
python -m unittest test_all_examples.py
```

Python 3 und Standardbibliothek reichen für diesen Abschnitt aus.
