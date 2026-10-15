# Messungen nummerieren

## Lernziel

`range(anzahl)` verwenden und die Zählung ab 0 von einer Nummerierung ab 1 unterscheiden.

## Aufgabe

Gib mit einer for-Schleife und range() für jede der {a} Messungen eine Zeile `Messung N` aus. Die Nummerierung beginnt bei 1. Gib danach einmal `Fertig.` aus. Definiere keine eigene Funktion.

## Datensätze und Beispielausgabe

Die Werte werden vom Zielsystem im Modul `dataset` bereitgestellt.
Lies sie mit `dataset.name.value`, zum Beispiel:

```python
import dataset
anzahl = int(dataset.a.value)
```

Lokale Beispielwerte in `dataset.py`:

```text
a = 4
```

Erwartete Ergebnisausgabe:

```text
Messung 1
Messung 2
Messung 3
Messung 4
Fertig.
```

## Dateien

- `answer.py`: ausführbare Musterlösung.
- `dataset.py`: lokale Beispielwerte; im Zielsystem wird dieses Modul bereitgestellt.
- `test_answer.py`: Ausgabetest mit `unittest` für den Wert aus `dataset.py`.

## Voraussetzungen

Python 3, nur Standardbibliothek. Die korrigierte `.lto`-Datei definiert `a`
als ganze Zahl zwischen 3 und 7 und zeigt den aktuellen Wert mit `{a}` an.
Der lokale Beispielwert 4 entspricht `datasetVariables` in dieser Datei.
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
python examples/03_loops_and_data/for_measurement_numbers/answer.py
python -m unittest discover -s examples/03_loops_and_data/for_measurement_numbers -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Lass die Lernenden vor dem Ausführen die Werte von `index` und die ausgegebenen Nummern gegenüberstellen. Bei `anzahl = 0` wird nur die Abschlussmeldung ausgegeben.

Die Tests prüfen die Ergebnisse. Die vorgeschriebene Schleifenform
prüft die Lehrkraft im kurzen Quelltext. Der Test vergleicht die Ergebnisausgabe
direkt für den in `dataset.py` hinterlegten Wert und überschreibt ihn nicht.

Für weitere Versuche kann der Wert in `a = DatasetVariable("a", 4)` geändert
und der Test erneut gestartet werden. Der Validator in der `.lto`-Datei prüft den aktuellen
Datensatz durch `import answer` und verwendet `RedirectedStdout` aus dem
vom Zielsystem bereitgestellten Modul `helpers`.
