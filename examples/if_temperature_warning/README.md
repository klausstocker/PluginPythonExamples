# Temperaturwarnung mit `if`

## Lernziel

Eine Anweisung mit `if` nur bei erfüllter Bedingung ausführen. Dabei einen
Standardwert festlegen und bei Bedarf überschreiben. Dies ist die erste
Aufgabe der Reihe: **if**, [if/else](../if_else_fan_control/README.md),
[if/elif/else](../if_elif_battery_status/README.md).

## Aufgabe

Ein Übungsprogramm bewertet die Temperatur eines Motors in °C.
Schreibe die Funktion `temperature_warning(temperature)`:

1. Speichere den Text `"OK"` in der Variable `message`.
2. Verwende ein `if`: Ab **60 °C**, einschließlich des Grenzwerts, wird
   `message` auf `"Temperature warning"` gesetzt.
3. Gib `message` nach der Verzweigung zurück.

Verwende hier noch kein `else`. Die Funktion gibt Text zurück und druckt ihn
nicht selbst aus. Achte auf den Doppelpunkt und die Einrückung nach `if`.

| Temperatur | Rückgabewert |
| --- | --- |
| 40 | `"OK"` |
| 60 | `"Temperature warning"` |
| 72 | `"Temperature warning"` |

## Dateien

- `answer.py`: Musterlösung mit Demonstrationsaufruf.
- `test_answer.py`: Tests für beide Ergebnisse und den Grenzwert.

## Voraussetzungen

Python 3, nur Standardbibliothek. Variablen, Vergleiche und einfache Funktionen
mit Parametern und `return` werden vorausgesetzt. Die Temperatur ist eine Zahl;
auch negative Werte sind zulässig. Der Grenzwert ist eine Vorgabe der Übung.
Eingabeprüfung und Schleifen sind nicht erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/if_temperature_warning/answer.py
python -m unittest discover -s examples/if_temperature_warning -p "test_*.py"
```

Der Demonstrationsaufruf gibt `Temperature warning` aus.
Alternativ im Beispielordner: `python -m unittest test_answer.py`.

## Hinweise für Lehrkräfte

Die Lernenden verfolgen den Wert von `message` vor und nach dem `if`.
Was passiert, wenn die Bedingung falsch ist? Warum steht `return` außerhalb
des eingerückten Blocks? Die Tests prüfen das Verhalten, einschließlich
59.9 und 60 °C. Die Verwendung eines einzelnen `if` wird im Quelltext geprüft.
