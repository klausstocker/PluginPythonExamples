# Lüftersteuerung mit `if/else`

## Lernziel

Mit `if/else` genau einen von zwei Zweigen ausführen. Dies ist die zweite
Aufgabe der Reihe: [if](../if_temperature_warning/README.md), **if/else**,
[if/elif/else](../if_elif_battery_status/README.md).

## Aufgabe

Ein Übungsprogramm bestimmt den Schaltbefehl für einen Lüfter anhand der
Temperatur in °C. Schreibe die Funktion `fan_command(temperature)`:

- Ab **40 °C**, einschließlich des Grenzwerts, ist der Befehl `"ON"`.
- Unter **40 °C** ist der Befehl `"OFF"`.

Verwende `if` und `else`, um den passenden Text in `command` zu speichern.
Gib `command` nach der Verzweigung zurück. Die Funktion soll nichts ausgeben.

| Temperatur | Rückgabewert |
| --- | --- |
| 25 | `"OFF"` |
| 40 | `"ON"` |
| 48 | `"ON"` |

## Dateien

- `answer.py`: Musterlösung mit Demonstrationsaufruf.
- `test_answer.py`: Tests für beide Zweige und den Grenzwert.

## Voraussetzungen

Python 3, nur Standardbibliothek. Variablen, Vergleiche, `if` und einfache
Funktionen mit Parametern und `return` werden vorausgesetzt. Die Temperatur
ist eine Zahl; auch negative Werte sind zulässig. Der Grenzwert ist eine
Vorgabe der Übung. Es wird nur ein Text berechnet, keine Hardware angesteuert.
Eingabeprüfung und Schleifen sind nicht erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/if_else_fan_control/answer.py
python -m unittest discover -s examples/if_else_fan_control -p "test_*.py"
```

Der Demonstrationsaufruf gibt `ON` aus.
Alternativ im Beispielordner: `python -m unittest test_answer.py`.

## Hinweise für Lehrkräfte

Warum benötigt `else` keine eigene Bedingung? Lassen Sie die Lernenden
erklären, warum `command` bei jeder Eingabe einen Wert erhält. Die Tests
prüfen insbesondere 39.9 und 40 °C. Ob `if/else` verwendet wird, wird im
Quelltext geprüft.
