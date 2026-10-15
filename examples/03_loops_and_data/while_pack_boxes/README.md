# Vollständige Kartons packen

## Lernziel

Eine Restmenge wiederholt reduzieren und die Grenze mit `>=` korrekt behandeln.

## Aufgabe

Es sind {bestand} Teile vorhanden. In einen Karton passen {kartongroesse} Teile. Packe mit einer while-Schleife so lange vollständige Kartons, wie genügend Teile vorhanden sind. Gib danach zwei Zeilen aus: `Kartons: N` und `Rest: N`. Verwende die Schleife statt `//` oder `%` und definiere keine eigene Funktion.

## Datensätze und Beispielausgabe

Die Werte werden vom Zielsystem im Modul `dataset` bereitgestellt.
Lies sie mit `dataset.name.value`, zum Beispiel:

```python
import dataset
bestand = int(dataset.bestand.value)
```

Lokale Beispielwerte in `dataset.py`:

```text
bestand = 23
kartongroesse = 5
```

Erwartete Ergebnisausgabe:

```text
Kartons: 4
Rest: 3
```

## Dateien

- `answer.py`: ausführbare Musterlösung.
- `dataset.py`: lokale Beispielwerte; im Zielsystem wird dieses Modul bereitgestellt.
- `test_answer.py`: Ausgabetest mit `unittest` für die Werte aus `dataset.py`.

## Voraussetzungen

Python 3, nur Standardbibliothek. Der Bestand ist eine nichtnegative ganze Zahl. Die Kartongröße ist eine positive ganze Zahl. Es werden nur vollständige Kartons gepackt.
Die lokale `dataset.py` verwendet `DatasetVariable` aus `examples/common.py`;
der Test verwendet dort auch `RedirectedStdout`. Beim Kopieren für eine lokale
Ausführung muss diese Hilfsdatei mit ihrer relativen Ordnerstruktur verfügbar
bleiben. Im Zielsystem werden `dataset` und `helpers` bereitgestellt.
Die Dataset-Werte erfüllen diese Voraussetzungen; eine Werteprüfung ist nicht Teil
der Aufgabe. Benötigt werden Variablen, Rechenoperatoren, Vergleiche,
`while`, `print()` und f-Strings.

Mit `int(dataset.name.value)` wird ein Dataset-Wert als ganze Zahl gelesen,
mit `float(dataset.name.value)` als Gleitkommazahl. Die Werte in der lokalen
Datei `dataset.py` können für eigene Versuche geändert werden. Das Programm
führt die Schleife auch beim Import aus, entsprechend der LeTTo-Vorlage.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/03_loops_and_data/while_pack_boxes/answer.py
python -m unittest discover -s examples/03_loops_and_data/while_pack_boxes -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Stelle den wiederholten Abzug anschließend den schon im Skript eingeführten Operatoren `//` und `%` gegenüber. Bei genau einer Kartongröße muss noch ein Durchlauf stattfinden.

Die Tests prüfen die Ergebnisse. Die vorgeschriebene Schleifenform
prüft die Lehrkraft im kurzen Quelltext. Der Test vergleicht die Ergebnisausgabe
direkt für die Werte aus `dataset.py`, ohne sie zu überschreiben. Für weitere
Versuche können diese Werte geändert und der Test erneut gestartet werden.

## LeTTo-Import

`Frage_while_pack_boxes.lto` enthält eine kurze Aufgabenangabe mit
Dataset-Platzhaltern und ein Startgerüst im Feld `indication`. Die vollständige
Musterlösung steht in `answer.py`. Der Validator verwendet `import answer`
und `RedirectedStdout` aus `helpers`.

`bestand`: 0 bis 50 und `kartongroesse`: 1 bis 10, jeweils ganzzahlig.
Die Kartongröße ist stets positiv; der Bestand sinkt mit jedem Durchlauf.
Enthalten sind ein leerer Bestand, eine exakt passende Kartongröße und Restmengen.

Die Datei enthält 40 Datensatzzeilen. Die erste Zeile entspricht den lokalen
Beispielwerten; die Beispielausgabe in der Angabe ist ausdrücklich diesen
Werten zugeordnet. Alle Dataset-Einheiten sind leere Strings. Physikalische
Einheiten bleiben im Aufgabentext und in der Ausgabe erhalten.
