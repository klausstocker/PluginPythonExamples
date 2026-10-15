# Papierdicke mit einer Funktion verdoppeln

## Lernziel

Exponentielles Wachstum schrittweise berechnen und eine Funktion wiederholt auf den aktuellen Zustand anwenden.

## Aufgabe

Ein Blatt Papier ist anfangs {dicke} mm dick. Berechne mit einer while-Schleife, wie oft es im vereinfachten Modell gefaltet werden muss, bis die Dicke mindestens {ziel} mm beträgt. Definiere `doppelte_dicke(dicke: float) -> float`, die `dicke * 2` zurückgibt, und rufe sie innerhalb der Schleife mit der aktuellen Dicke auf. Übernimm jeweils den Rückgabewert und zähle die Faltungen. Gib zwei Zeilen aus: `Faltungen: N` und `Dicke: X.XXX mm`, mit drei Nachkommastellen für die Dicke. Das Ziel darf überschritten werden. Verwende keine Logarithmusformel.

## Datensätze und Beispielausgabe

Die Werte werden vom Zielsystem im Modul `dataset` bereitgestellt.
Lies sie mit `dataset.name.value`, zum Beispiel:

```python
import dataset
dicke = float(dataset.dicke.value)
```

Lokale Beispielwerte in `dataset.py`:

```text
dicke = 0.1
ziel = 1.0
```

Erwartete Ergebnisausgabe:

```text
Faltungen: 4
Dicke: 1.600 mm
```

## Dateien

- `answer.py`: ausführbare Musterlösung.
- `dataset.py`: lokale Beispielwerte; im Zielsystem wird dieses Modul bereitgestellt.
- `test_answer.py`: Ausgabetest mit `unittest` für die Werte aus `dataset.py`.

## Voraussetzungen

Python 3, nur Standardbibliothek. Anfangsdicke und Zieldicke sind positive, endliche Zahlen in mm; verwende gewöhnliche Unterrichtswerte. Das Modell setzt eine exakte Verdopplung voraus und ignoriert die praktische Begrenzung der Faltbarkeit.
Die lokale `dataset.py` verwendet `DatasetVariable` aus `examples/common.py`;
der Test verwendet dort auch `RedirectedStdout`. Beim Kopieren für eine lokale
Ausführung muss diese Hilfsdatei mit ihrer relativen Ordnerstruktur verfügbar
bleiben. Im Zielsystem werden `dataset` und `helpers` bereitgestellt.
Die Dataset-Werte erfüllen diese Voraussetzungen; eine Werteprüfung ist nicht Teil
der Aufgabe. Benötigt werden Variablen, Rechenoperatoren, Vergleiche,
`while`, `print()` und f-Strings. Hinzu kommen eigene Funktionen mit Parametern und `return`.

Mit `int(dataset.name.value)` wird ein Dataset-Wert als ganze Zahl gelesen,
mit `float(dataset.name.value)` als Gleitkommazahl. Die Werte in der lokalen
Datei `dataset.py` können für eigene Versuche geändert werden. Das Programm
führt die Schleife auch beim Import aus, entsprechend der LeTTo-Vorlage.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/03_loops_and_data/while_paper_folding/answer.py
python -m unittest discover -s examples/03_loops_and_data/while_paper_folding -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Lass zunächst die Dicke nach jeder Faltung vorhersagen. Markiere anschließend den Funktionsaufruf im Schleifenkörper und die Zuweisung des Rückgabewerts.

Die Tests prüfen die Ergebnisse. Die vorgeschriebene Schleifenform und den Funktionsaufruf im Schleifenkörper
prüft die Lehrkraft im kurzen Quelltext. Der Test vergleicht die Ergebnisausgabe
direkt für die Werte aus `dataset.py`, ohne sie zu überschreiben. Für weitere
Versuche können diese Werte geändert und der Test erneut gestartet werden.

## LeTTo-Import

`Frage_while_paper_folding.lto` enthält eine kurze Aufgabenangabe mit
Dataset-Platzhaltern und ein Startgerüst im Feld `indication`. Die vollständige
Musterlösung steht in `answer.py`. Der Validator verwendet `import answer`
und `RedirectedStdout` aus `helpers`.

`dicke` ist auf 0.1 mm festgelegt; `ziel` ist eine ganze Zahl von 1 bis 8 mm.
Die Lösung liest beide Werte als Gleitkommazahlen. Die Anfangsdicke ist strikt
positiv und wächst durch Verdopplung, sodass jede exportierte Zieldicke nach
endlich vielen Schritten erreicht oder überschritten wird.

Die Datei enthält 40 Datensatzzeilen. Die erste Zeile entspricht den lokalen
Beispielwerten; die Beispielausgabe in der Angabe ist ausdrücklich diesen
Werten zugeordnet. Alle Dataset-Einheiten sind leere Strings. Physikalische
Einheiten bleiben im Aufgabentext und in der Ausgabe erhalten.
