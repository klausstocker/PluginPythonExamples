# Winkel zwischen zwei Vektoren in 3D

## Lernziel

NumPy-Arrays als dreidimensionale Vektoren verwenden und aus Skalarprodukt
und Vektorlängen einen Winkel berechnen. Type Hints machen die erwarteten
Eingaben und den Rückgabewert in der Funktionssignatur sichtbar.

## Aufgabe

Zwei Richtungsvektoren beschreiben beispielsweise die Ausrichtung eines
Roboterwerkzeugs und eine gewünschte Bewegungsrichtung im selben Koordinatensystem.
Schreibe die Funktion:

```python
import numpy as np
from numpy.typing import NDArray


def winkel_zwischen_vektoren(
    vektor_a: NDArray[np.float64], vektor_b: NDArray[np.float64]
) -> float:
    ...
```

Beide Eingaben sind eindimensionale NumPy-Arrays mit genau drei Komponenten
`[x, y, z]`, also der Form `(3,)`. Erzeuge sie beispielsweise mit
`np.array([2.0, 0.0, 1.0], dtype=np.float64)`.
`NDArray[np.float64]` beschreibt ein NumPy-Array mit 64-Bit-Gleitkommazahlen;
die Form `(3,)` wird zusätzlich im Code geprüft. Type Hints selbst prüfen
oder konvertieren zur Laufzeit keine Eingaben.

Gib den kleineren, ungerichteten Winkel als Python-`float` in **Grad**, zwischen
0 und 180, zurück. Die Funktion soll die Eingaben nicht verändern.

Aus der Beziehung zwischen Skalarprodukt und Winkel folgt:

```text
a · b = ||a|| * ||b|| * cos(alpha)
alpha = arccos((a · b) / (||a|| * ||b||))
```

1. Prüfe die Form und die Endlichkeit der Komponenten.
2. Berechne beide Vektorlängen mit `np.linalg.norm`.
3. Lehne Nullvektoren mit `ValueError` ab: Sie haben keine Richtung.
4. Berechne das Skalarprodukt mit `np.dot` und teile durch das Produkt der Längen.
5. Begrenze den Kosinus mit `np.clip` auf `[-1.0, 1.0]`, um kleine Rundungsfehler abzufangen.
6. Berechne mit `np.arccos` den Winkel und wandle ihn mit `np.degrees` in Grad um.

Auch eine falsche Form oder nicht endliche Komponenten (`NaN`, Unendlich)
sollen zu `ValueError` führen.

| Vektor a | Vektor b | Winkel |
| --- | --- | --- |
| `[1, 0, 0]` | `[0, 1, 0]` | 90 Grad |
| `[1, 0, 0]` | `[2, 0, 0]` | 0 Grad |
| `[1, 0, 0]` | `[-2, 0, 0]` | 180 Grad |
| `[1, 0, 0]` | `[1, 1, 0]` | 45 Grad |

## Bezug zum Skript

Das Beispiel baut auf [Robotics_Script.pdf](../../Robotics_Script.pdf) auf:

- §1.1.5, „Length and unit vectors“, gedruckte Seite 5: Vektorlänge mit `np.linalg.norm`.
- §1.1.6, „Dot product“, gedruckte Seite 6: dreidimensionales Skalarprodukt und
  die Beziehung `a · b = ||a|| * ||b|| * cos(alpha)`.
- §1.1.6.1, ebenfalls Seite 6: Die Demonstrationsvektoren `[3, 1, 1]` und
  `[1, 3, 2]` werden für dieses Rechenbeispiel übernommen.

Die Formel wird hier nach dem Winkel aufgelöst. Wie im Skript werden Vektoren
als eindimensionale Arrays dargestellt. Eine grafische Darstellung ist für
diese Aufgabe nicht erforderlich.

## Dateien

- `answer.py` enthält die typisierte Musterlösung und einen Demonstrationsaufruf.
- `test_answer.py` prüft bekannte Winkel, Symmetrie, positive Skalierung,
  ungültige Eingaben und unveränderte Eingabearrays mit `unittest`.

## Voraussetzungen

Python 3.8 oder neuer und eine zur Python-Version passende NumPy-Version
(mindestens 1.21 für `numpy.typing.NDArray`). NumPy ist in der zentralen
`requirements.txt` eingetragen. Weitere Pakete sind nicht erforderlich.
Vorausgesetzt werden Funktionen, Type Hints, Vektoren und das Skalarprodukt.

Die Aufgabe verwendet reelle Gleitkommazahlen üblicher Größenordnung.
Extrem große oder kleine Komponenten, bei denen die Normberechnung über- oder
unterläuft, gehören nicht zum Umfang dieser Einführung.

## Ausführen und testen

Im Repository-Hauptordner mit dem Python-Interpreter der virtuellen Umgebung:

```bash
python -m pip install -r requirements.txt
python examples/vector_angle_3d/answer.py
python -m unittest discover -s examples/vector_angle_3d -p "test_*.py"
```

Der Demonstrationsaufruf gibt ungefähr `Winkel: 49.86 Grad` aus.

Alternativ im Beispielordner, nachdem NumPy installiert wurde:

```bash
python answer.py
python -m unittest test_answer.py
```

Beim Kopieren des Beispielordners in ein anderes Projekt genügt
`python -m pip install "numpy>=1.21"` zur Installation der Abhängigkeit.

## Hinweise für Lehrkräfte

Lassen Sie zuerst Winkel für parallele, entgegengesetzte und senkrechte Vektoren
vorhersagen. Anschließend können Lernende die Länge eines Vektors durch positive
Skalierung verändern und beobachten, dass der Winkel gleich bleibt.
Die Tests verwenden andere Vektoren als die Demonstration und vergleichen
Winkel näherungsweise, weil Gleitkommaoperationen Rundungsfehler verursachen.

Die [NumPy-Dokumentation zu `arccos`](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html)
beschreibt den reellen Eingabebereich `[-1, 1]` und die Ausgabe im Bogenmaß.
Die Umrechnung in Grad ist daher ein eigener Rechenschritt.
