# 4. Funktionen

Neun selbstständige Beispiele passend zum Kapitel Funktionen im Informatikskript.
Die Reihenfolge führt von `def` und `return` über Type Hints und Standardwerte
zum Kombinieren von Funktionen und zur trigonometrischen Anwendung.
Die grundlegenden Aufrufe verwenden Positionsargumente; das Trigonometrie-Beispiel
ergänzt benannte Argumente als optionale Vertiefung.

## Empfohlene Reihenfolge

1. [Scheinleistung als Funktion](apparent_power/README.md): Eine Funktion definieren, mit mehreren Argumenten aufrufen und einen lokalen Ergebniswert zurückgeben.
2. [Energieverbrauch berechnen](energy_consumption/README.md): Parameter und Rückgabewert mit Type Hints dokumentieren; Einheiten umrechnen.
3. [Energiekosten mit Standardtarif](energy_cost/README.md): Einen unveränderlichen Standardwert für einen Parameter verwenden.
4. [Spannungsbereich als Funktion](voltage_check/README.md): Eine Funktion mit booleschem Rückgabewert und Standardgrenzen schreiben.
5. [Vom Energieverbrauch zu den Kosten](consumption_to_cost/README.md): Den Rückgabewert einer Funktion an eine andere Funktion weitergeben.
6. [Turmhöhe mit dem Tangens](tower_height/README.md): Trigonometrie mit Parametern, Rückgabewert, Type Hints und einer Standardmesshöhe verbinden.
7. [Pascalsches Dreieck ausgeben](pascal_triangle/README.md): Eine Funktion mit Zeilenanzahl als Parameter und Rückgabetyp `str` schreiben; den zurückgegebenen String auf stdout ausgeben.
8. [Primzahlen in einem Bereich finden](prime_numbers/README.md): Eine Hilfsfunktion zum Prüfen einer Zahl verwenden und alle Primzahlen im Bereich als Liste zurückgeben.
9. [Die 16 logischen Funktionen mit zwei Eingängen](truth_table_two_inputs/README.md): Wahrheitstabellen als Binärzahlen nummerieren und alle Varianten mit `and`, `or` und `not` umsetzen.

Im nächsten Kapitel folgt [Bestellung mit Dataclasses prüfen](../05_dataclasses/order_dataclasses/README.md).

## Tests

Jedes Beispiel enthält seine Testbefehle im README. Alle Beispiele:

```bash
python -m unittest test_all_examples.py
```

Python 3 und Standardbibliothek reichen für diesen Abschnitt aus.
