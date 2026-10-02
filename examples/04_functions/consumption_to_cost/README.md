# Vom Energieverbrauch zu den Kosten

## Lernziel

Den Rückgabewert einer Funktion an eine andere Funktion weitergeben.

## Aufgabe

Definiere `energie_kwh(leistung_watt: float, dauer_stunden: float) -> float` und `energiekosten(energie_kwh: float, preis_pro_kwh: float = 0.30) -> float`. Schreibe außerdem `betriebskosten(leistung_watt: float, dauer_stunden: float, preis_pro_kwh: float = 0.30) -> float`. Diese Funktion soll zuerst `energie_kwh` und danach `energiekosten` aufrufen und die Kosten zurückgeben.

## Dateien

- `answer.py` enthält die Musterlösung und eine Demonstration.
- `test_answer.py` prüft die Ergebnisse mit anderen Eingaben und Grenzfällen.

## Voraussetzungen

Python 3, nur Standardbibliothek. Variablen und Grundrechenarten. Konstante Leistung; alle Eingaben nichtnegativ. Der Standardtarif ist fiktiv. Alle Funktionsaufrufe verwenden Positionsargumente; benannte Argumente sind nicht erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/04_functions/consumption_to_cost/answer.py
python -m unittest discover -s examples/04_functions/consumption_to_cost -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Die beiden vorherigen Energieaufgaben bilden die Grundlage. Dieses Beispiel enthält dennoch alle Funktionen und lässt sich separat kopieren. Prüfe im Quelltext, dass betriebskosten die beiden Hilfsfunktionen aufruft.
