# Abkühlung mit einer Funktion simulieren

## Lernziel

Den Rückgabewert einer Funktion als neuen Zustand übernehmen und eine Zielbedingung prüfen.

## Aufgabe

Ein Körper hat anfangs {temperatur} °C, die Umgebung hat {umgebung} °C. Simuliere die Abkühlung, bis die Temperatur höchstens {ziel} °C beträgt. Definiere `abkuehlen(temperatur: float, umgebung: float) -> float`, die `(temperatur + umgebung) / 2` zurückgibt. Rufe die Funktion innerhalb einer while-Schleife mit der jeweils aktuellen Temperatur auf und übernimm den Rückgabewert. Zähle die Schritte. Gib zwei Zeilen aus: `Schritte: N` und `Temperatur: X.XX °C`, mit zwei Nachkommastellen für die Temperatur.

## Datensätze und Beispielausgabe

Die Werte werden vom Zielsystem im Modul `dataset` bereitgestellt.
Lies sie mit `dataset.name.value`, zum Beispiel:

```python
import dataset
temperatur = float(dataset.temperatur.value)
```

Lokale Beispielwerte in `dataset.py`:

```text
temperatur = 100.0
umgebung = 20.0
ziel = 30.0
```

Erwartete Ergebnisausgabe:

```text
Schritte: 3
Temperatur: 30.00 °C
```

## Dateien

- `answer.py`: ausführbare Musterlösung.
- `dataset.py`: lokale Beispielwerte; im Zielsystem wird dieses Modul bereitgestellt.
- `test_answer.py`: Ausgabetest mit `unittest` für die Werte aus `dataset.py`.

## Voraussetzungen

Python 3, nur Standardbibliothek. Alle Dataset-Werte sind endliche Zahlen in °C mit `umgebung < ziel` und `temperatur >= umgebung`. Verwende gewöhnliche Unterrichtswerte mit mindestens 1 °C Abstand zwischen Ziel und Umgebung. Das vereinfachte Modell halbiert die Temperaturdifferenz je Schritt und beschreibt keine genaue physikalische Abkühlungszeit.
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
python examples/03_loops_and_data/while_cooling/answer.py
python -m unittest discover -s examples/03_loops_and_data/while_cooling -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Die Funktion muss die jeweils aktuelle Temperatur erhalten. Besprich, warum das wiederholte Übergeben der Starttemperatur keinen Fortschritt erzeugt. Das Ziel muss oberhalb der Umgebung liegen, da das Modell die Umgebung nur annähert.

Die Tests prüfen die Ergebnisse. Die vorgeschriebene Schleifenform und den Funktionsaufruf im Schleifenkörper
prüft die Lehrkraft im kurzen Quelltext. Der Test vergleicht die Ergebnisausgabe
direkt für die Werte aus `dataset.py`, ohne sie zu überschreiben. Für weitere
Versuche können diese Werte geändert und der Test erneut gestartet werden.

## LeTTo-Import

`Frage_while_cooling.lto` enthält eine kurze Aufgabenangabe mit
Dataset-Platzhaltern und ein Startgerüst im Feld `indication`. Die vollständige
Musterlösung steht in `answer.py`. Der Validator verwendet `import answer`
und `RedirectedStdout` aus `helpers`.

`temperatur`: 20 bis 100, `umgebung`: 10 bis 20 und `ziel`: 25 bis 40.
Alle exportierten Werte sind ganzzahlig, die Lösung liest sie als Gleitkommazahlen.
Stets gilt `umgebung < ziel` und `temperatur >= umgebung`. Die Differenz zur
Umgebung halbiert sich je Schritt; da das Ziel oberhalb der Umgebung liegt,
endet die Schleife. Ein Ziel gleich der Umgebung wird nicht erzeugt.
Enthalten sind auch schon erreichte und unterschrittene Ziele.

Die Datei enthält 40 Datensatzzeilen. Die erste Zeile entspricht den lokalen
Beispielwerten; die Beispielausgabe in der Angabe ist ausdrücklich diesen
Werten zugeordnet. Alle Dataset-Einheiten sind leere Strings. Physikalische
Einheiten bleiben im Aufgabentext und in der Ausgabe erhalten.
