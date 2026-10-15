# Einen Behälter schrittweise füllen

## Lernziel

Eine Schleife durch einen Zielvergleich beenden und eine mögliche Überschreitung des Ziels erkennen.

## Aufgabe

Ein Behälter enthält anfangs {fuellstand} Liter. Pro Schritt kommen {zufluss} Liter hinzu. Wiederhole das Füllen mit einer while-Schleife, bis mindestens {ziel} Liter enthalten sind, und zähle die Schritte. Ein letzter Schritt wird vollständig ausgeführt; das Ziel darf dadurch überschritten werden. Gib danach zwei Zeilen aus: `Schritte: N` und `Füllstand: X.X l`, mit einer Nachkommastelle für den Füllstand. Definiere keine eigene Funktion.

## Datensätze und Beispielausgabe

Die Werte werden vom Zielsystem im Modul `dataset` bereitgestellt.
Lies sie mit `dataset.name.value`, zum Beispiel:

```python
import dataset
fuellstand = float(dataset.fuellstand.value)
```

Lokale Beispielwerte in `dataset.py`:

```text
fuellstand = 2.0
ziel = 10.0
zufluss = 3.0
```

Erwartete Ergebnisausgabe:

```text
Schritte: 3
Füllstand: 11.0 l
```

## Dateien

- `answer.py`: ausführbare Musterlösung.
- `dataset.py`: lokale Beispielwerte; im Zielsystem wird dieses Modul bereitgestellt.
- `test_answer.py`: Ausgabetest mit `unittest` für die Werte aus `dataset.py`.

## Voraussetzungen

Python 3, nur Standardbibliothek. Füllstand und Ziel sind nichtnegativ. `zufluss` ist strikt positiv. Alle Größen sind endliche Zahlen in Litern; der Zufluss ist so groß, dass er den gespeicherten Füllstand erhöht. Es handelt sich um ein Rechenmodell ohne Hardware.
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
python examples/03_loops_and_data/while_fill_tank/answer.py
python -m unittest discover -s examples/03_loops_and_data/while_fill_tank -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Die Anzahl der Schritte wird aus dem Verlauf ermittelt. Besprich, warum `fuellstand != ziel` bei einem übersprungenen Ziel eine Endlosschleife verursachen könnte.

Die Tests prüfen die Ergebnisse. Die vorgeschriebene Schleifenform
prüft die Lehrkraft im kurzen Quelltext. Der Test vergleicht die Ergebnisausgabe
direkt für die Werte aus `dataset.py`, ohne sie zu überschreiben. Für weitere
Versuche können diese Werte geändert und der Test erneut gestartet werden.

## LeTTo-Import

`Frage_while_fill_tank.lto` enthält eine kurze Aufgabenangabe mit
Dataset-Platzhaltern und ein Startgerüst im Feld `indication`. Die vollständige
Musterlösung steht in `answer.py`. Der Validator verwendet `import answer`
und `RedirectedStdout` aus `helpers`.

`fuellstand`: 0 bis 15, `ziel`: 5 bis 12 und `zufluss`: 1 bis 4.
Alle exportierten Werte sind ganzzahlig, die Lösung liest sie als Gleitkommazahlen.
Der Zufluss ist stets positiv; dadurch endet die Schleife auch bei einem
übersprungenen Ziel. Enthalten sind auch bereits erreichte und überschrittene Ziele.

Die Datei enthält 40 Datensatzzeilen. Die erste Zeile entspricht den lokalen
Beispielwerten; die Beispielausgabe in der Angabe ist ausdrücklich diesen
Werten zugeordnet. Alle Dataset-Einheiten sind leere Strings. Physikalische
Einheiten bleiben im Aufgabentext und in der Ausgabe erhalten.
