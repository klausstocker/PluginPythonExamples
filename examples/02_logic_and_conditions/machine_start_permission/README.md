# Startfreigabe einer simulierten Anlage

## Lernziel

`and`, `or` und `not` mit klaren Klammern kombinieren.

## Aufgabe

Eine simulierte Anlage erhält eine Startfreigabe, wenn die Tür geschlossen ist, kein Stoppsignal aktiv ist und mindestens einer von zwei Starttastern gedrückt ist. Berechne `startfreigabe` aus `tuer_geschlossen`, `stoppsignal_aktiv`, `taster_links` und `taster_rechts` und gib sie aus.

## Dateien

- `answer.py` enthält die Musterlösung und eine Demonstration.
- `test_answer.py` prüft die Ergebnisse mit anderen Eingaben und Grenzfällen.

## Voraussetzungen

Python 3, nur Standardbibliothek. Variablen, Zahlen, Vergleiche und Wahrheitswerte. Keine eigenen Funktionen, Verzweigungen oder Schleifen in der Lösung erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/02_logic_and_conditions/machine_start_permission/answer.py
python -m unittest discover -s examples/02_logic_and_conditions/machine_start_permission -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Nur ein Logikmodell für den Unterricht. Beide gedrückten Taster erfüllen den Startwunsch ebenfalls. Die Tests tauschen die Eingaben vor der Markierung `# Auswertung` aus und führen den Lösungscode danach aus. Diese Markierung bitte beibehalten.
