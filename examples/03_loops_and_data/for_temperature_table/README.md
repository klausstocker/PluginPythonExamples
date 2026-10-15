# Temperaturtabelle mit einer Funktion

## Lernziel

Einheitenumrechnung als Funktion definieren und sie bei jedem Schleifendurchlauf verwenden.

## Aufgabe

Definiere `fahrenheit(celsius: float) -> float` mit der Formel `celsius * 9 / 5 + 32`. Die Funktion gibt nur den berechneten Wert zurück. Durchlaufe Celsiuswerte von {start} bis vor {stopp} mit einer Schrittweite von {schrittweite}. Verwende eine for-Schleife mit range() und rufe innerhalb der Schleife für jeden Wert `fahrenheit` auf. Gib `N °C = X.X °F` mit einer Nachkommastelle für den Fahrenheitwert aus.

## Datensätze und Beispielausgabe

Die Werte werden vom Zielsystem im Modul `dataset` bereitgestellt.
Lies sie mit `dataset.name.value`, zum Beispiel:

```python
import dataset
start = int(dataset.start.value)
```

Lokale Beispielwerte in `dataset.py`:

```text
start = 0
stopp = 31
schrittweite = 10
```

Erwartete Ergebnisausgabe:

```text
0 °C = 32.0 °F
10 °C = 50.0 °F
20 °C = 68.0 °F
30 °C = 86.0 °F
```

## Dateien

- `answer.py`: ausführbare Musterlösung.
- `dataset.py`: lokale Beispielwerte; im Zielsystem wird dieses Modul bereitgestellt.
- `test_answer.py`: Ausgabetest mit `unittest` für die Werte aus `dataset.py`.

## Voraussetzungen

Python 3, nur Standardbibliothek. Alle Bereichsangaben sind ganze Zahlen. Die Schrittweite ist ungleich null. Die Stoppgrenze wird nicht verarbeitet. Die Aufgabe verwendet Celsius- und Fahrenheitwerte als Rechenmodell.
Die lokale `dataset.py` verwendet `DatasetVariable` aus `examples/common.py`;
der Test verwendet dort auch `RedirectedStdout`. Beim Kopieren für eine lokale
Ausführung muss diese Hilfsdatei mit ihrer relativen Ordnerstruktur verfügbar
bleiben. Im Zielsystem werden `dataset` und `helpers` bereitgestellt.
Die Dataset-Werte erfüllen diese Voraussetzungen; eine Werteprüfung ist nicht Teil
der Aufgabe. Benötigt werden Variablen, Rechenoperatoren, Vergleiche,
`for` und `range()`, `print()` und f-Strings. Hinzu kommen eigene Funktionen mit Parametern und `return`.

Mit `int(dataset.name.value)` wird ein Dataset-Wert als ganze Zahl gelesen,
mit `float(dataset.name.value)` als Gleitkommazahl. Die Werte in der lokalen
Datei `dataset.py` können für eigene Versuche geändert werden. Das Programm
führt die Schleife auch beim Import aus, entsprechend der LeTTo-Vorlage.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/03_loops_and_data/for_temperature_table/answer.py
python -m unittest discover -s examples/03_loops_and_data/for_temperature_table -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Vergleiche die Aufgaben Leistungstabelle und Temperaturtabelle: Die Schleifenstruktur bleibt gleich, während die aufgerufene Berechnungsfunktion wechselt.

Die Tests prüfen die Ergebnisse. Die vorgeschriebene Schleifenform und den Funktionsaufruf im Schleifenkörper
prüft die Lehrkraft im kurzen Quelltext. Der Test vergleicht die Ergebnisausgabe
direkt für die Werte aus `dataset.py`, ohne sie zu überschreiben. Für weitere
Versuche können diese Werte geändert und der Test erneut gestartet werden.

## LeTTo-Import

`Frage_for_temperature_table.lto` verwendet die überarbeitete Roboteraufgabe
als Formatvorlage: kurze Angabe mit Dataset-Platzhaltern, 40 Datensatzzeilen
und ein Funktionsgerüst im Feld `indication`. Die vollständige Musterlösung
steht in `answer.py`. Der Validator verwendet `import answer` und
`RedirectedStdout` aus `helpers`.

Die ganzzahligen Bereiche sind `start`: 0 bis 10, `stopp`: 31 bis 51 und
`schrittweite`: 5 bis 10. Die Vorschauwerte entsprechen der ersten Zeile
(0, 31, 10). Die Beispielausgabe ist ausdrücklich diesen Werten zugeordnet.
Dataset-Einheiten sind überall leere Strings; °C und °F stehen im Text und
in der Programmausgabe.
