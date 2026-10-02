# Genau eine Betriebsart gewählt

## Lernziel

Bei booleschen Werten XOR mit `!=` ausdrücken und mit `or` vergleichen.

## Aufgabe

Die booleschen Variablen `handbetrieb` und `automatikbetrieb` zeigen die gewählten Betriebsarten. Speichere in `mindestens_eine_betriebsart`, ob mindestens eine gewählt ist, und in `genau_eine_betriebsart`, ob genau eine gewählt ist. Gib beide Ergebnisse aus.

## Dateien

- `answer.py` enthält die Musterlösung und eine Demonstration.
- `test_answer.py` prüft die Ergebnisse mit anderen Eingaben und Grenzfällen.

## Voraussetzungen

Python 3, nur Standardbibliothek. Variablen, Zahlen, Vergleiche und Wahrheitswerte. Keine eigenen Funktionen, Verzweigungen oder Schleifen in der Lösung erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/02_logic_and_conditions/exclusive_operating_mode/answer.py
python -m unittest discover -s examples/02_logic_and_conditions/exclusive_operating_mode -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Lass alle vier Kombinationen vorhersagen. Wenn beide Betriebsarten gewählt sind, unterscheiden sich ODER und XOR. Die Tests tauschen die Eingaben vor der Markierung `# Auswertung` aus und führen den Lösungscode danach aus. Diese Markierung bitte beibehalten.
