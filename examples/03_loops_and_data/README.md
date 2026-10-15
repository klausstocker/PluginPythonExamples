# 3. Loops and data

Practice repeating calculations, processing collections, and reading measured
values from a file. Learners should already understand variables, comparisons,
and conditions. Introduce lists, tuples, and file access as each task needs them.

## Recommended order

1. [Range datasets](for_range_datasets/README.md): iterate over ranges and collect results.
2. [Count dial stops at zero](count_pointing_at_zero/README.md): process instructions and update a running state.
3. [Minimum BMI](minimum_bmi/README.md): search structured records for the smallest calculated value.
4. [Minimal distance](minimal_distance/README.md): compare pairs of points using nested loops.
5. [Power from CSV](power_from_csv/README.md): read measurements from a file and calculate average power.

[Filter people](filter_people/README.md) is an additional exercise on tuple
unpacking, age comparisons, and filtering with `or`; print matching names to stdout.

[SQLite library](sqlite_library/README.md) introduces a many-to-many relationship
with books, customers, and lends; query who borrowed a book and on which dates.

Each example documents its input format, assumptions, and required concepts.
Keep any accompanying data files with the example when copying it.

## Zehn Einstiegsaufgaben zu Schleifen

Diese Aufgaben orientieren sich an den Abschnitten „Funktionen“ und „Schleifen“
in `C:\TMP\HTL\RoboticsScript\Infomatik_Script.md`. Jede Aufgabe enthält eine
deutsche Aufgabenbeschreibung, eine ausführbare Musterlösung und eigene Tests.
Python 3 und die Standardbibliothek reichen aus; die Beispiele benötigen keinen
Zugriff auf das Skript und können einzeln kopiert werden.

### Fünf Aufgaben mit `for ... in range(...)`

| Aufgabe | Schwerpunkt | Eigene Funktion im Schleifenkörper |
| --- | --- | --- |
| [Messungen nummerieren](for_measurement_numbers/README.md) | `range(anzahl)`, Nummerierung ab 1 | Nein |
| [Roboterschlitten](for_robot_positions/README.md) | Positionen, eingeschlossene letzte Schrittnummer | Nein |
| [Versuchslaufzeiten](for_total_runtime/README.md) | Laufende Summe und veränderliche Dauer | Nein |
| [Leistungstabelle](for_power_table/README.md) | Strombereich mit Schrittweite, Leistung berechnen | `leistung_watt(spannung, strom)` |
| [Temperaturtabelle](for_temperature_table/README.md) | Celsiuswerte durchlaufen und umrechnen | `fahrenheit(celsius)` |

### Fünf Aufgaben mit `while`

| Aufgabe | Schwerpunkt | Eigene Funktion im Schleifenkörper |
| --- | --- | --- |
| [Behälter füllen](while_fill_tank/README.md) | Ziel erreichen oder überschreiten | Nein |
| [Kartons packen](while_pack_boxes/README.md) | Bestand reduzieren, vollständige Kartons zählen | Nein |
| [Quersumme](while_digit_sum/README.md) | Letzte Ziffer mit `%` und `//` verarbeiten | Nein |
| [Abkühlung](while_cooling/README.md) | Temperaturzustand bis zum Ziel aktualisieren | `abkuehlen(temperatur, umgebung)` |
| [Papierdicke](while_paper_folding/README.md) | Wiederholte Verdopplung bis zur Zieldicke | `doppelte_dicke(dicke)` |

Jeweils die ersten drei Aufgaben kommen ohne eigene Funktionsdefinition aus.
In den letzten beiden muss die angegebene Funktion in jedem Schleifendurchlauf
aufgerufen und ihr Rückgabewert verwendet werden. Die Reihenfolge innerhalb
beider Gruppen eignet sich als Lernfolge. Alle Werte werden über
`dataset.<name>.value` gelesen. Für lokale Aufrufe enthält jeder Ordner eine
eigene `dataset.py` mit Beispielwerten; im Zielsystem stellt LeTTo dieses Modul
bereit. Wertebereiche und Abbruchbedingungen stehen im jeweiligen README.

### LeTTo-Import

Die Datei [Fragen_Schleifen_LeTTo.xml](../../Fragen_Schleifen_LeTTo.xml) enthält
alle zehn Aufgaben. Zusätzlich liegt in jedem der zehn Beispielordner eine
`Frage_<ordnername>.lto` für den Einzelimport. Beide Varianten verwenden die
XML-Struktur der `.lto`-Vorlagen im Repository-Hauptordner: `<letto>` mit Fragen
vom Typ `MoodleClozeCalc`, dem Python-Plugin und der Teilfrage `[Q0]`.

Jede Frage enthält die Aufgabenbeschreibung, Vorschaucode im Plugin-Feld
`indication` und die Tests im Feld
`validation` zur automatischen Bewertung. Dataset-Variablen sind sowohl in
`datasetVariables` als auch als XML-`dataset`-Elemente hinterlegt, entsprechend
der Vorlage `Frage_for_in_range.lto`. Die Aufgaben zeigen die aktuellen Werte
als LeTTo-Platzhalter an. Wertebereiche, Einheiten und die jeweils 40
Datensatz-Items stehen in der XML-Datei. Die bereits überarbeiteten Aufgaben
verwenden auch variable Datensätze. Beim Roboterschlitten enthält `indication`
ein Startgerüst; die vollständige Musterlösung steht in `answer.py`.

Für neue und überarbeitete Aufgaben werden Dataset-Einheiten als leerer String
gespeichert (`unit: ""` in der Plugin-Konfiguration, leeres `einheit`-Element
im XML und `DatasetVariable(..., "")` lokal). Physikalische Einheiten stehen
bei Bedarf im Aufgabentext und in der Programmausgabe.

Die Tests der zehn Einstiegsaufgaben prüfen direkt den aktuellen Datensatz.
Weitere Werte und Grenzfälle werden über die exportierten Datensatzzeilen
geprüft; die lokalen Tests überschreiben die Dataset-Werte nicht.
Sie benötigen keine zusätzlichen Dateien aus diesem Repository; das native
`dataset`-Modul wird vom Zielsystem bereitgestellt. Die lokale `dataset.py`
wird nicht mit exportiert. Musterlösungen führen die Schleife beim Import aus,
wie die Vorlage. Die Bewertung erfolgt anhand der Tests,
das Linting hat kein Gewicht. Die geforderte Schleifenform und Funktionsaufrufe
prüft die Lehrkraft im Quelltext.

## Run tests

From the repository root, for example:

```bash
python -m unittest discover -s examples/03_loops_and_data/minimum_bmi -p "test_*.py"
```

Each example README gives its task and test command. Run all chapters with
`python -m unittest test_all_examples.py`.

Previous: [Logic and conditions](../02_logic_and_conditions/README.md).
