# Akkustatus mit `if/elif/else`

## Lernziel

Mit `if/elif/else` drei Wertebereiche unterscheiden und die Reihenfolge der
Bedingungen verstehen. Dies ist die dritte Aufgabe der Reihe:
[if](../if_temperature_warning/README.md),
[if/else](../if_else_fan_control/README.md), **if/elif/else**.

## Aufgabe

Ein Übungsprogramm bewertet den Akkuladestand eines Roboters.
Schreibe die Funktion `battery_status(charge_percent)`:

| Ladestand | Rückgabewert |
| --- | --- |
| Unter 20 % | `"Critical"` |
| Ab 20 %, aber unter 50 % | `"Charge soon"` |
| Ab 50 % | `"Ready"` |

Verwende `if`, `elif` und `else`. Prüfe zuerst, ob der Ladestand unter 20 %
liegt, und danach, ob er unter 50 % liegt. Speichere den Text in `status`
und gib ihn nach der Verzweigung zurück. Die Funktion soll nichts ausgeben.
Beispielsweise ergibt 35 % den Text `"Charge soon"`.

## Dateien

- `answer.py`: Musterlösung mit Demonstrationsaufruf.
- `test_answer.py`: Tests für alle drei Zweige, beide Schwellen und die
  Endpunkte 0 und 100 %.

## Voraussetzungen

Python 3, nur Standardbibliothek. Variablen, Vergleiche, `if/else` und einfache
Funktionen mit Parametern und `return` werden vorausgesetzt. Der Ladestand
ist eine Zahl von 0 bis 100, einschließlich der Endpunkte; Dezimalwerte sind
zulässig. Die Schwellen sind Vorgaben der Übung. Eingabeprüfung, Schleifen
und zusätzliche Pakete sind nicht erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/02_logic_and_conditions/if_elif_battery_status/answer.py
python -m unittest discover -s examples/02_logic_and_conditions/if_elif_battery_status -p "test_*.py"
```

Der Demonstrationsaufruf gibt `Charge soon` aus.
Alternativ im Beispielordner: `python -m unittest test_answer.py`.

## Hinweise für Lehrkräfte

Bei 12 % sind beide Vergleiche wahr, trotzdem wird nur der erste Zweig
ausgeführt. Lassen Sie die Lernenden erklären, warum im `elif` keine
zusätzliche Prüfung auf mindestens 20 % nötig ist. Was würde sich ändern,
wenn zuerst auf unter 50 % geprüft würde? Die Tests prüfen die Ergebnisse;
die geforderte Verzweigungsstruktur wird im Quelltext geprüft.
