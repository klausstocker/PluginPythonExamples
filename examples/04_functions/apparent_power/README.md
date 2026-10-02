# Scheinleistung als Funktion

## Lernziel

Eine Funktion definieren, mit mehreren Argumenten aufrufen und einen lokalen Ergebniswert zurückgeben.

## Aufgabe

Schreibe `scheinleistung(wirkleistung, blindleistung)`. Berechne mit `math.sqrt()` die Scheinleistung in VA aus Wirkleistung in W und Blindleistung in var. Speichere das Ergebnis lokal in `scheinleistung_va` und gib es mit `return` zurück.

## Dateien

- `answer.py` enthält die Musterlösung und eine Demonstration.
- `test_answer.py` prüft die Ergebnisse mit anderen Eingaben und Grenzfällen.

## Voraussetzungen

Python 3, nur Standardbibliothek. Variablen und Grundrechenarten. Sinusfürmige Spannung und sinusfürmiger Strom im stationären Betrieb; Wirkleistung nichtnegativ. Alle Funktionsaufrufe verwenden Positionsargumente; benannte Argumente sind nicht erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/04_functions/apparent_power/answer.py
python -m unittest discover -s examples/04_functions/apparent_power -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Die Aufrufe verwenden verschiedene Verbraucher. Vergleiche Parameter, Argumente und lokale Variable.
