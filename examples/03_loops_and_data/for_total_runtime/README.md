# Laufzeiten einer Versuchsreihe addieren

## Lernziel

Eine Summe vor der Schleife initialisieren und in jedem Durchlauf fortschreiben.

## Aufgabe

Eine Versuchsreihe umfasst {anzahl} Versuche. Der erste Versuch dauert {startdauer} Sekunden, jeder folgende Versuch um {zuwachs} Sekunden länger. Addiere mit einer for-Schleife mit range() alle Versuchsdauern. Gib danach `Gesamtdauer: X.X s` aus. Bei null Versuchen beträgt die Gesamtdauer 0.0 Sekunden. Definiere keine eigene Funktion und verwende keine fertige Summenformel.

## Datensätze und Beispielausgabe

Die Werte werden vom Zielsystem im Modul `dataset` bereitgestellt.
Lies sie mit `dataset.name.value`, zum Beispiel:

```python
import dataset
anzahl = int(dataset.anzahl.value)
```

Lokale Beispielwerte in `dataset.py`:

```text
anzahl = 4
startdauer = 2.0
zuwachs = 0.5
```

Erwartete Ergebnisausgabe:

```text
Gesamtdauer: 11.0 s
```

## Dateien

- `answer.py`: ausführbare Musterlösung.
- `dataset.py`: lokale Beispielwerte; im Zielsystem wird dieses Modul bereitgestellt.
- `test_answer.py`: Ausgabetest mit `unittest` für die Werte aus `dataset.py`.

## Voraussetzungen

Python 3, nur Standardbibliothek. `anzahl` ist eine nichtnegative ganze Zahl; `startdauer` und `zuwachs` sind nichtnegative Zahlen in Sekunden. Bei null Versuchen ist die Gesamtdauer null.
Die lokale `dataset.py` verwendet `DatasetVariable` aus `examples/common.py`;
der Test verwendet dort auch `RedirectedStdout`. Beim Kopieren für eine lokale
Ausführung muss diese Hilfsdatei mit ihrer relativen Ordnerstruktur verfügbar
bleiben. Im Zielsystem werden `dataset` und `helpers` bereitgestellt.
Die Dataset-Werte erfüllen diese Voraussetzungen; eine Werteprüfung ist nicht Teil
der Aufgabe. Benötigt werden Variablen, Rechenoperatoren, Vergleiche,
`for` und `range()`, `print()` und f-Strings.

Mit `int(dataset.name.value)` wird ein Dataset-Wert als ganze Zahl gelesen,
mit `float(dataset.name.value)` als Gleitkommazahl. Die Werte in der lokalen
Datei `dataset.py` können für eigene Versuche geändert werden. Das Programm
führt die Schleife auch beim Import aus, entsprechend der LeTTo-Vorlage.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/03_loops_and_data/for_total_runtime/answer.py
python -m unittest discover -s examples/03_loops_and_data/for_total_runtime -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Lass eine Tabelle mit `dauer` und `gesamtdauer` nach jedem Durchlauf ausfüllen. Die Erhöhung von `dauer` muss nach dem Addieren stehen.

Die Tests prüfen die Ergebnisse. Die vorgeschriebene Schleifenform
prüft die Lehrkraft im kurzen Quelltext. Der Test vergleicht die Ergebnisausgabe
direkt für die Werte aus `dataset.py`, ohne sie zu überschreiben. Für weitere
Versuche können diese Werte geändert und der Test erneut gestartet werden.

Die Beispielversuche dauern 2.0, 2.5, 3.0 und 3.5 Sekunden; zusammen sind das
11.0 Sekunden. Der Zuwachs nach dem letzten Versuch wird nicht mehr addiert.

## LeTTo-Import

`Frage_for_total_runtime.lto` enthält eine kurze Aufgabenangabe mit
Dataset-Platzhaltern und einen Kommentar als Startgerüst im Feld `indication`.
Die vollständige Musterlösung steht in `answer.py`. Der Validator verwendet
`import answer` und `RedirectedStdout` aus `helpers`.

Die Datei enthält 40 Datensatzzeilen: `anzahl` liegt zwischen 0 und 8,
`startdauer` zwischen 1 und 5 Sekunden; `zuwachs` beträgt 0.5 Sekunden.
Die erste Zeile entspricht den lokalen Vorschauwerten (4, 2.0, 0.5).
Enthalten sind auch null Versuche und ein einzelner Versuch.
Alle Dataset-Einheiten sind leere Strings. Die Einheit `s` steht im
Aufgabentext und in der Programmausgabe.
