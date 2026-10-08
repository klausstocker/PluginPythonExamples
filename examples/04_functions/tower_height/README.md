# Turmhöhe mit dem Tangens berechnen

## Lernziel

Eine eigene Funktion mit Parametern, lokalen Variablen und Rückgabewert schreiben.
Type Hints und einen Standardwert verwenden. Eine trigonometrische Formel
in Python umsetzen und Gradmaß in Bogenmaß umrechnen.

## Aufgabe

Du möchtest die Höhe eines Turms bestimmen, ohne ihn zu besteigen. Du misst den
waagerechten Abstand zum Fuß des Turms und den Winkel zwischen der Waagerechten
und der Sichtlinie zur Turmspitze. Das Messgerät befindet sich über dem Boden.

Im rechtwinkligen Dreieck gilt:

$$
\tan(\alpha) = \frac{\text{Höhenunterschied}}{\text{Abstand}}
$$

Damit ergibt sich die gesamte Turmhöhe:

$$
h = d \cdot \tan(\alpha) + h_\text{Messgerät}
$$

Schreibe folgende Funktion:

```python
def turmhoehe(
    abstand_m: float, winkel_grad: float, messhoehe_m: float = 1.5
) -> float:
    ...
```

1. Wandle den Winkel mit `math.radians()` von Grad in Bogenmaß um.
2. Berechne den Höhenunterschied mit `math.tan()`.
3. Addiere die Messhöhe und gib die Turmhöhe in Metern mit `return` zurück.
4. Rufe die Funktion für unterschiedliche Messungen auf: einmal mit der
   Standardmesshöhe von 1,5 m und einmal mit einer eigenen Messhöhe.
5. Speichere die Rückgabewerte und gib sie außerhalb der Funktion mit Einheit
   und zwei Nachkommastellen aus. Runde nicht innerhalb der Funktion.

Beispiel: Bei 20 m Abstand, 35° Höhenwinkel und 1,5 m Messhöhe ergibt sich
eine Turmhöhe von ungefähr 15,50 m.

## Dateien

- `answer.py` enthält die Musterlösung und zwei Demonstrationen.
- `draw_triangle.py` zeichnet das beschriftete Messdreieck mit Matplotlib.
- `test_answer.py` vergleicht die Ergebnisse mit der Referenzfunktion `correct()` anhand anderer Messdaten,
  den Standardwert und wiederholte Funktionsaufrufe.

## Voraussetzungen

Python 3, nur Standardbibliothek (`math` und `unittest`). Grundkenntnisse zu
rechtwinkligen Dreiecken und Tangens. `math.tan()` erwartet Bogenmaß.
Der Turm steht senkrecht; Messort und Turmfuß liegen auf gleicher Bodenhöhe.
Der Abstand ist positiv, die Messhöhe nichtnegativ und der Winkel liegt zwischen
0° (einschließlich) und 90° (ausschließlich). Gültige Eingaben werden vorausgesetzt;
eine Eingabeprüfung ist nicht Teil der Aufgabe.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/04_functions/tower_height/answer.py
python -m unittest discover -s examples/04_functions/tower_height -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

### Diagramm zeichnen

Die optionale Visualisierung benötigt zusätzlich Matplotlib (in der
repositoryweiten `requirements.txt` enthalten):

```bash
python -m pip install -r requirements.txt
python examples/04_functions/tower_height/draw_triangle.py
```

Das Skript zeigt das Diagramm in einem Fenster und speichert es als
`tower_triangle.png` im Beispielordner. Abstand, Höhenwinkel und Messhöhe
können im Aufruf von `zeichne_dreieck()` am Skriptende geändert werden.
Die Zeichnung zeigt Ankathete, Gegenkathete, Hypotenuse, Winkel, Messhöhe,
Gesamthöhe und die Tangensformel. Für ein nicht entartetes Dreieck muss der
Winkel hier größer als 0° und kleiner als 90° sein.
Zum Speichern ohne Fenster kann das Skript mit `MPLBACKEND=Agg` ausgeführt werden
(in PowerShell vorher `$env:MPLBACKEND = "Agg"` setzen).

### Didaktische Hinweise

Das Beispiel greift die Abschnitte zu Funktionen in `Infomatik_Script.md` auf:
`def` definiert die Berechnung; Parameter erhalten bei jedem Aufruf neue Werte.
`winkel_rad` und `hoehenunterschied_m` sind lokale Variablen. `return` liefert
das Ergebnis zur weiteren Verarbeitung, während `print()` die Ausgabe übernimmt.
Type Hints dokumentieren die Typen und erzwingen keine Prüfung zur Laufzeit.
Der Standardwert gehört zum letzten Parameter und kann beim Aufruf ersetzt werden.

Als Einstieg kann die Funktion zunächst ohne Type Hints und mit drei erforderlichen
Parametern geschrieben werden. Danach werden Typangaben und Standardwert ergänzt.
Bei Gleitkommazahlen prüfen die Tests mit `assertAlmostEqual()` statt auf exakte
Gleichheit. Die Referenzfunktion `correct()` berechnet die erwarteten Werte
unabhängig von der eingereichten Funktion in `answer.py`.

Optionale Vertiefung passend zu „Advanced: Benannte Argumente“ im Skript:

```python
hoehe_m = turmhoehe(messhoehe_m=1.7, winkel_grad=40.0, abstand_m=30.0)
```

Lass die Lernenden erklären, weshalb diese Reihenfolge möglich ist und warum
die Messhöhe zur berechneten Gegenkathete addiert werden muss.
