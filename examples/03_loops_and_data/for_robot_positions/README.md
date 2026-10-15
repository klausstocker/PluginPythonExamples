# Positionen eines Roboterschlittens

## Lernziel

Mit `range(1, anzahl + 1)` eine eingeschlossene letzte Schrittnummer abbilden und die Position berechnen.

## Aufgabe

Ein Roboterschlitten startet bei 0 mm und bewegt sich {anzahl} Schritte mit einer Schrittweite von {schrittweite} mm. Verwende eine for-Schleife mit range(), um die Position nach jedem Schritt zu berechnen und auszugeben. Die Schrittnummern beginnen bei 1. Gib die Startposition nicht aus und definiere keine eigene Funktion. Verwende pro Zeile das Format `Schritt N: X.X mm`, also eine Nachkommastelle für die Position.

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
schrittweite = 2.9
```

Erwartete Ergebnisausgabe:

```text
Schritt 1: 2.9 mm
Schritt 2: 5.8 mm
Schritt 3: 8.7 mm
Schritt 4: 11.6 mm
```

## Dateien

- `answer.py`: ausführbare Musterlösung.
- `dataset.py`: lokale Beispielwerte; im Zielsystem wird dieses Modul bereitgestellt.
- `test_answer.py`: Ausgabetest mit `unittest` für die Werte aus `dataset.py`.

## Voraussetzungen

Python 3, nur Standardbibliothek. `anzahl` ist eine nichtnegative ganze Zahl, `schrittweite` eine positive Zahl in mm. Das Programm berechnet Positionen eines Modells; es benötigt keine Roboterhardware.
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
python examples/03_loops_and_data/for_robot_positions/answer.py
python -m unittest discover -s examples/03_loops_and_data/for_robot_positions -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Die Startposition wird nicht ausgegeben. Vergleiche `range(1, anzahl)` mit `range(1, anzahl + 1)`: Welche letzte Position würde fehlen?

Die Tests prüfen die Ergebnisse. Die vorgeschriebene Schleifenform
prüft die Lehrkraft im kurzen Quelltext. Der Test vergleicht die Ergebnisausgabe
direkt für die Werte aus `dataset.py`, ohne sie zu überschreiben. Für weitere
Versuche können diese Werte geändert und der Test erneut gestartet werden.

## LeTTo-Import

`Frage_for_robot_positions.lto` folgt der überarbeiteten
`Frage_for_power_table.lto`: kurze Aufgabenangabe mit Dataset-Platzhaltern,
variable Wertebereiche und einen Kommentar als Startgerüst im Feld `indication`.
Die vollständige Musterlösung steht in `answer.py`. Der Validator im Feld
`validation` verwendet `import answer` und `RedirectedStdout` aus `helpers`.

`anzahl` liegt zwischen 3 und 7; `schrittweite` enthält Fließkommawerte
mit der LeTTo-Bereichsangabe `F2:2-7` (gespeicherte Werte: 2.1 bis 6.9).
Die Datei enthält 40 Datensatzzeilen; die Vorschauwerte entsprechen
der ersten Zeile (4 Schritte mit 2.9 mm Schrittweite). Die Beispielausgabe in der
LeTTo-Angabe bezieht sich ausdrücklich auf 4 Schritte mit 2 mm Schrittweite. Für andere
Datensätze werden die erwarteten Ergebnisse aus den aktuellen Werten berechnet.
Dataset-Einheiten sind in Python und XML leere Strings. Die Angabe und die
Programmausgabe enthalten weiterhin `mm`.
