# Quersumme einer Teilenummer

## Lernziel

Mit `% 10` die letzte Ziffer verarbeiten und mit `// 10` die noch zu bearbeitende Zahl verkleinern.

## Aufgabe

Berechne die Quersumme der Teilenummer {teilenummer} mit einer while-Schleife. Addiere in jedem Durchlauf die letzte Ziffer zur Summe und entferne diese Ziffer durch ganzzahlige Division. Gib `Quersumme: N` aus. Verwende keine Zeichenkettenverarbeitung und definiere keine eigene Funktion. Für die Teilenummer 0 ist das Ergebnis 0.

## Datensätze und Beispielausgabe

Die Werte werden vom Zielsystem im Modul `dataset` bereitgestellt.
Lies sie mit `dataset.name.value`, zum Beispiel:

```python
import dataset
teilenummer = int(dataset.teilenummer.value)
```

Lokale Beispielwerte in `dataset.py`:

```text
teilenummer = 2047
```

Erwartete Ergebnisausgabe:

```text
Quersumme: 13
```

## Dateien

- `answer.py`: ausführbare Musterlösung.
- `dataset.py`: lokale Beispielwerte; im Zielsystem wird dieses Modul bereitgestellt.
- `test_answer.py`: Ausgabetest mit `unittest` für die Werte aus `dataset.py`.

## Voraussetzungen

Python 3, nur Standardbibliothek. Die Teilenummer ist eine nichtnegative ganze Zahl. Führende Nullen sind für die Quersumme unerheblich. Vorausgesetzt werden die Operatoren `%` und `//` aus dem Skript.
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
python examples/03_loops_and_data/while_digit_sum/answer.py
python -m unittest discover -s examples/03_loops_and_data/while_digit_sum -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Lass die Werte von `rest`, `letzte_ziffer` und `quersumme` tabellarisch verfolgen. Die Abbruchbedingung ergibt sich aus der verbleibenden Zahl.

Die Tests prüfen die Ergebnisse. Die vorgeschriebene Schleifenform
prüft die Lehrkraft im kurzen Quelltext. Der Test vergleicht die Ergebnisausgabe
direkt für die Werte aus `dataset.py`, ohne sie zu überschreiben. Für weitere
Versuche können diese Werte geändert und der Test erneut gestartet werden.

## LeTTo-Import

`Frage_while_digit_sum.lto` enthält eine kurze Aufgabenangabe mit
Dataset-Platzhaltern und ein Startgerüst im Feld `indication`. Die vollständige
Musterlösung steht in `answer.py`. Der Validator verwendet `import answer`
und `RedirectedStdout` aus `helpers`.

`teilenummer`: ganze Zahlen von 0 bis 99999.
Enthalten sind 0, eine einzelne Ziffer und Zahlen mit inneren Nullen.
Durch `// 10` wird die verbleibende Zahl in jedem Durchlauf kleiner und endet bei 0.

Die Datei enthält 40 Datensatzzeilen. Die erste Zeile entspricht den lokalen
Beispielwerten; die Beispielausgabe in der Angabe ist ausdrücklich diesen
Werten zugeordnet. Alle Dataset-Einheiten sind leere Strings. Physikalische
Einheiten bleiben im Aufgabentext und in der Ausgabe erhalten.
