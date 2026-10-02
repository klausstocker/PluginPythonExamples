# Spannung im erlaubten Bereich

## Lernziel

Vergleiche und `and` ohne eigene Funktionen verwenden.

## Aufgabe

Prüfe eine Spannung in V. Der Übungsbereich reicht von 210 V bis 250 V einschließlich beider Grenzen. Speichere das Ergebnis in `spannung_erlaubt` und gib es aus.

## Dateien

- `answer.py` enthält die Musterlösung und eine Demonstration.
- `test_answer.py` prüft die Ergebnisse mit anderen Eingaben und Grenzfällen.

## Voraussetzungen

Python 3, nur Standardbibliothek. Variablen, Zahlen, Vergleiche und Wahrheitswerte. Keine eigenen Funktionen, Verzweigungen oder Schleifen in der Lösung erforderlich.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/02_logic_and_conditions/voltage_range/answer.py
python -m unittest discover -s examples/02_logic_and_conditions/voltage_range -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Grenzwerte sind Vorgaben der Übung. Besprich den Unterschied zwischen `>` und `>=`. Die Tests tauschen die Eingaben vor der Markierung `# Auswertung` aus und führen den Lösungscode danach aus. Diese Markierung bitte beibehalten.
