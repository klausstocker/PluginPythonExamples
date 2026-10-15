# Vorwärtskinematik eines planaren Zweiachsroboters

## Lernziel

Eine Funktion mit zwei Eingaben und zwei Rückgabewerten schreiben.
Relative Gelenkwinkel von absoluten Armrichtungen unterscheiden und
Sinus und Kosinus zur Berechnung einer Endpunktposition anwenden.

## Aufgabe

Ein Roboter bewegt zwei starre Arme in der xy-Ebene. Der erste Arm ist
100 mm lang, der zweite 80 mm. Schreibe folgende Funktion:

```python
def forward_kinematics(alpha: float, beta: float) -> tuple[float, float] | None:
    ...
```

Die Eingaben sind Gelenkwinkel in Grad. Die Funktion gibt die Endpunktposition
`(x, y)` in Millimetern zurück, ohne innerhalb der Funktion zu runden oder
etwas auszugeben. Bei nicht endlichen Winkeln (`nan`, `inf`, `-inf`)
gibt sie `None` zurück.

Es gelten folgende Konventionen:

- Das erste Gelenk liegt im Ursprung. Die positive x-Achse zeigt nach rechts,
  die positive y-Achse nach oben.
- `alpha` ist der Winkel des ersten Arms zur positiven Welt-x-Achse.
- `beta` ist der relative Winkel des zweiten Arms zum ersten Arm.
  Bei `beta = 0°` ist der Roboter vollständig gestreckt.
- Positive Winkel drehen gegen den Uhrzeigersinn. Beide Gelenke können frei
  drehen; negative Winkel und Winkel außerhalb von 0° bis 360° sind erlaubt.
- Der gesuchte Punkt ist das Ende des zweiten Arms, ohne zusätzlichen
  Werkzeugversatz. Kollisionen werden nicht betrachtet.

1. Prüfe mit `math.isfinite()`, ob beide Winkel endlich sind.
2. Bestimme die absolute Richtung beider Arme. Der zweite Arm hat die Richtung
   `alpha + beta`, nicht nur `beta`.
3. Wandle die benötigten Winkel mit `math.radians()` ins Bogenmaß um.
4. Berechne für jeden Arm die x- und y-Komponente und addiere die Komponenten.
5. Gib die Koordinaten als Tupel zurück.

Für einen Arm mit Länge $l$ und absolutem Richtungswinkel $\theta$ gilt:

$$
\vec{v} = \begin{bmatrix}l\cos\theta\\l\sin\theta\end{bmatrix}.
$$

Die Endpunktposition ist die Summe der beiden Armvektoren. Leite daraus
die Gleichungen für `x` und `y` ab. Python verwendet in Winkelfunktionen Bogenmaß.

Beispiel: `forward_kinematics(0.0, 90.0)` liefert ungefähr `(100.0, 80.0)`.

## Dateien

- `answer.py` enthält die Musterlösung mit festen Armlängen und Beispielaufruf.
- `test_answer.py` prüft gestreckte und gefaltete Arme, relative Winkel,
  schräge Stellungen in allen Quadranten und ungültige Eingaben.
  Die Referenzfunktion `correct()` dreht den Endpunkt aus dem lokalen
  Koordinatensystem des ersten Arms ins Weltkoordinatensystem.

## Voraussetzungen

Python 3.10 oder neuer, nur Standardbibliothek (`math` und `unittest`).
Grundkenntnisse zu Funktionen, Tupeln und Winkelfunktionen.
Die Eingaben sind Zahlen; andere Datentypen werden nicht geprüft.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/06_robotics/forward_kinematics_2d/answer.py
python -m unittest discover -s examples/06_robotics/forward_kinematics_2d -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Gib den Lernenden die Aufgabenbeschreibung und die Tests; `answer.py` dient
als Musterlösung. Als Start genügt die Funktionssignatur mit `pass` und
ein Import von `math`. Bei geänderten Armlängen müssen auch Testdaten und
Aufgabenbeschreibung angepasst werden.

Die Geometrie entspricht dem Beispiel zur
[inversen Kinematik](../inverse_kinematics_2d/README.md). Als Erweiterung können
Lernende erst die inverse Kinematik auf eine erreichbare Zielposition anwenden
und anschließend mit dieser Funktion prüfen, ob die berechneten Winkel
wieder zum Ziel führen. Dabei können unterschiedliche Gelenkkonfigurationen
dieselbe Endpunktposition ergeben.

Die Testwerte unterscheiden sich vom Beispielaufruf.
`assertAlmostEqual()` berücksichtigt Rundungsfehler von Gleitkommazahlen.
