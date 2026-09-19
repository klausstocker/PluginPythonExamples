# Beide Grenzwerte erreicht

## Lernziel

Vergleiche mit `>=` zu booleschen Werten auswerten und mit `and`
die geforderte Entscheidung formulieren. Die Aufgabe gehört zu einer Reihe
von drei fast gleichen Aufgaben: [and](../logical_and/README.md),
[or](../logical_or/README.md), [not](../logical_not/README.md).

## Aufgabe

Ein Übungsprogramm wertet zwei Messwerte eines Motors aus:

- `temperatur`: Temperatur in °C; auffällig ab **60 °C**.
- `strom`: Stromstärke in A; auffällig ab **10 A**.

Die Grenzwerte selbst zählen bereits als auffällig.

Schreibe die Funktion `pruefe_messwerte(temperatur, strom)`.
Speichere zuerst die beiden Vergleiche in `temperatur_auffaellig` und
`strom_auffaellig`. Verknüpfe diese Werte mit `and` gemäß folgender Regel:

Gib genau dann `True` zurück, wenn **beide** Messwerte ihren Grenzwert erreicht oder überschritten haben.

In allen anderen Fällen soll die Funktion `False` zurückgeben.
Sie soll einen booleschen Wert zurückgeben, keinen Text und keine Ausgabe.

Ein einzelner auffälliger Messwert reicht hier nicht aus.

| Temperatur | Strom | Erwartetes Ergebnis |
| --- | --- | --- |
| 45 °C | 7 A | `False` |
| 45 °C | 13 A | `False` |
| 80 °C | 7 A | `False` |
| 80 °C | 13 A | `True` |

## Dateien

- `answer.py` enthält die Musterlösung und einen Demonstrationsaufruf.
- `test_answer.py` enthält zehn Tests mit `unittest`, einschließlich aller
  Wahrheitswertkombinationen und der Grenzfälle.

## Voraussetzungen

Python 3, nur Standardbibliothek. Vorausgesetzt werden Variablen, Vergleiche,
`True`/`False` und einfache Funktionen mit Parametern und `return`.
Die Messwerte sind nichtnegative Zahlen in den angegebenen Einheiten.
Die Grenzwerte sind Vorgaben dieser Übung. Eingabeprüfung, Schleifen und
zusätzliche Pakete sind nicht erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/logical_and/answer.py
python -m unittest discover -s examples/logical_and -p "test_*.py"
```

Der Demonstrationsaufruf mit 70 °C und 11 A gibt `True` aus.

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Alle drei Aufgaben verwenden dieselbe Funktionssignatur, dieselben Vergleiche
und dieselben Testeingaben. Nur die logische Verknüpfung und die erwarteten
Ergebnisse ändern sich. Die Lernenden können zuerst die Ergebnistabelle
vorhersagen und anschließend ihre Lösung testen.

Die Tests verwenden andere Messwerte als der Demonstrationsaufruf und prüfen
auch exakt 60 °C, exakt 10 A und Werte knapp darunter. So fallen ein
vertauschter Operator und `>` statt `>=` auf. Die Tests prüfen das Verhalten;
ob der geforderte Operator verwendet wurde, lässt sich im kurzen Quelltext
prüfen.
