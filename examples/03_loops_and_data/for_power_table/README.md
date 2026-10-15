# Leistungstabelle mit einer Funktion

## Lernziel

Eine Berechnungsfunktion für jeden Wert eines ganzzahligen Bereichs innerhalb der Schleife aufrufen.

## Aufgabe

Definiere `leistung_watt(spannung: float, strom: float) -> float`. Die Funktion gibt `spannung * strom` zurück und erzeugt keine Ausgabe. Berechne bei einer Spannung von {spannung} V die Leistung für Stromwerte von {start} A bis vor {stopp} A mit einer Schrittweite von {schrittweite} A. Verwende eine for-Schleife mit range() und rufe die Funktion innerhalb der Schleife auf. Gib je eine Zeile `I = N A: X.X W` aus. Die Stoppgrenze ist ausgeschlossen.

## Datensätze und Beispielausgabe

Die Werte werden vom Zielsystem im Modul `dataset` bereitgestellt.
Lies sie mit `dataset.name.value`, zum Beispiel:

```python
import dataset
spannung = float(dataset.spannung.value)
```

Lokale Beispielwerte in `dataset.py`:

```text
spannung = 12
start = 2
stopp = 10
schrittweite = 2
```

Erwartete Ergebnisausgabe:

```text
I = 2 A: 24.0 W
I = 4 A: 48.0 W
I = 6 A: 72.0 W
I = 8 A: 96.0 W
```

## Dateien

- `answer.py`: ausführbare Musterlösung.
- `dataset.py`: lokale Beispielwerte; im Zielsystem wird dieses Modul bereitgestellt.
- `test_answer.py`: Ausgabetest mit `unittest` für die Werte aus `dataset.py`.

## Voraussetzungen

Python 3, nur Standardbibliothek. Die Spannung ist nichtnegativ. Die Bereichsgrenzen sind ganze Zahlen; die ganzzahlige Schrittweite darf positiv oder negativ, aber nicht null sein. Negative Ströme und Leistungen sind hier vorzeichenbehaftete Rechenwerte.
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
python examples/03_loops_and_data/for_power_table/answer.py
python -m unittest discover -s examples/03_loops_and_data/for_power_table -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Die selbst definierte Funktion wird bei jeder Iteration mit einem anderen Stromwert aufgerufen. Lass die Lernenden die Aufrufstelle im Schleifenkörper markieren. Die Formel gilt hier für Gleichspannung beziehungsweise einen rein ohmschen Verbraucher.

Die Tests prüfen die Ergebnisse. Die vorgeschriebene Schleifenform und den Funktionsaufruf im Schleifenkörper
prüft die Lehrkraft im kurzen Quelltext. Der Test vergleicht die Ergebnisausgabe
direkt für die Werte aus `dataset.py`, ohne sie zu überschreiben. Für weitere
Versuche können diese Werte geändert und der Test erneut gestartet werden.

## LeTTo-Import

`Frage_for_power_table.lto` verwendet die Struktur der korrigierten Datei
`Frage_for_measurement_numbers.lto`. Der Validator importiert die Abgabe mit
`import answer`, liest die aktuellen Dataset-Werte und vergleicht die Ausgabe
mit einer Referenzimplementierung. `RedirectedStdout` wird im Zielsystem aus
`helpers` importiert. Der vollständige Beispielcode steht im Feld `indication`.
