# Energiekosten mit Standardtarif

## Lernziel

Einen unveränderlichen Standardwert für einen Parameter verwenden.

## Aufgabe

Schreibe `energiekosten(energie_kwh: float, preis_pro_kwh: float = 0.30) -> float`. Gib Energie mal Preis als Kosten in Euro zurück. Zeige Aufrufe mit einem Argument und mit zwei Positionsargumenten.

## Dateien

- `answer.py` enthält die Musterlösung und eine Demonstration.
- `test_answer.py` prüft die Ergebnisse mit anderen Eingaben und Grenzfällen.

## Voraussetzungen

Python 3, nur Standardbibliothek. Variablen und Grundrechenarten. Energie und Preis sind nichtnegativ. 0,30 Euro/kWh ist ein fiktiver Übungstarif. Alle Funktionsaufrufe verwenden Positionsargumente; benannte Argumente sind nicht erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/04_functions/energy_cost/answer.py
python -m unittest discover -s examples/04_functions/energy_cost -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Ein weggelassenes zweites Argument verwendet den Standardtarif. Ein zweites Positionsargument ersetzt ihn. Runde erst bei der Ausgabe, nicht in der Funktion.
