# Inverse Kinematik eines planaren Zweiachsroboters

## Lernziel

Eine Funktion mit zwei Eingaben und zwei Rückgabewerten schreiben. Den
Kosinussatz und trigonometrische Funktionen zur Berechnung von Gelenkwinkeln
anwenden und Gradmaß von Bogenmaß unterscheiden.

## Aufgabe

Ein Roboter bewegt zwei starre Arme in der xy-Ebene. Der erste Arm ist
100 mm lang, der zweite 80 mm. Schreibe folgende Funktion:

```python
def inverse_kinematik(x: float, y: float) -> tuple[float, float] | None:
    ...
```

Die Eingaben sind die Zielkoordinaten in Millimetern. Die Funktion gibt
`(alpha, beta)` in Grad zurück, ohne innerhalb der Funktion zu runden oder
etwas auszugeben. Ist der Zielpunkt nicht erreichbar, gibt sie `None` zurück.

Es gelten folgende Konventionen:

- Das erste Gelenk liegt im Ursprung. Die positive x-Achse zeigt nach rechts,
  die positive y-Achse nach oben.
- `alpha` ist der Winkel des ersten Arms zur positiven x-Achse.
- `beta` ist der relative Winkel des zweiten Arms zum ersten Arm.
  Bei `beta = 0°` ist der Roboter vollständig gestreckt.
- Positive Winkel drehen gegen den Uhrzeigersinn. Verwende die Lösung
  mit `0° <= beta <= 180°`. Mechanische Gelenkgrenzen werden nicht berücksichtigt.

1. Prüfe, ob die Koordinaten endlich sind und der Abstand zum Ursprung zwischen
   20 mm und 180 mm einschließlich liegt. Andernfalls gib `None` zurück.
2. Bestimme den Innenwinkel am Gelenk mit dem Kosinussatz und leite daraus `beta` ab.
3. Bestimme den Innenwinkel an der Basis und die Richtung zum Ziel.
   Verwende für die Zielrichtung `math.atan2()`, damit alle vier Quadranten funktionieren.
   Leite aus den Winkelbeziehungen `alpha` ab.
4. Wandle beide Winkel mit `math.degrees()` in Grad um und gib sie als Tupel zurück.

Das Armdreieck besteht aus der Basis O, dem Gelenk G und dem Ziel P.
Seine Seitenlängen sind $l_1$, $l_2$ und $r$, wobei $r^2=x^2+y^2$.
Der Innenwinkel am Gelenk heißt $\gamma$, der Innenwinkel an der Basis $\delta$.
Der Kosinussatz liefert:

$$
r^2 = l_1^2 + l_2^2 - 2l_1l_2\cos\gamma
$$

$$
l_2^2 = l_1^2 + r^2 - 2l_1r\cos\delta
$$

Der Gelenkwinkel und der Innenwinkel ergänzen sich zu einem gestreckten Winkel:

$$
\gamma + \beta = 180^\circ
$$

Die Richtung $\theta$ von der Basis zum Ziel erfüllt:

$$
x = r\cos\theta, \qquad y = r\sin\theta
$$

Für die gewählte Gelenkkonfiguration setzt sie sich aus dem Winkel des ersten
Arms und dem Innenwinkel an der Basis zusammen:

$$
\theta = \alpha + \delta \quad (\text{mod } 360^\circ)
$$

Stelle die Beziehungen selbst nach den gesuchten Winkeln um.
Die Winkelfunktionen in Python verwenden Bogenmaß. Begrenze den berechneten Kosinus vor
`acos()` auf `[-1, 1]`, um Rundungsfehler an den Arbeitsbereichsgrenzen abzufangen.

Beispiel: Für `x = 100 mm` und `y = 80 mm` ergibt sich
`alpha = 0°` und `beta = 90°`.

## Dateien

- `answer.py` enthält die Musterlösung mit festen Armlängen und einem Beispielaufruf.
- `draw_robot.py` zeichnet Arme, Gelenke, Zielkoordinaten und die Zusammenhänge im Dreieck.
- `solution.mac` berechnet die Gelenkwinkel in Maxima Schritt für Schritt.
- `test_answer.py` prüft bekannte Winkel, Ziele in allen Quadranten,
  Arbeitsbereichsgrenzen und ungültige Eingaben. Die Referenzfunktion `correct(x, y)`
  berechnet die Winkel unabhängig mit den Innenwinkeln des Armdreiecks und
  liefert für unerreichbare Ziele ebenfalls `None`. Die Vorwärtskinematik prüft
  unabhängig, ob die berechneten Winkel zur Zielposition führen.

## Voraussetzungen

Python 3.10 oder neuer, nur Standardbibliothek (`math` und `unittest`).
Grundkenntnisse zu Funktionen, Tupeln, Kosinussatz und Winkelfunktionen.
Die Armlängen sind positive Konstanten; für dieses Beispiel ist der erste Arm
länger als der zweite. Die Zielkoordinaten sind Zahlen.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/06_robotics/inverse_kinematics_2d/answer.py
python -m unittest discover -s examples/06_robotics/inverse_kinematics_2d -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

### Diagramm zeichnen

Die optionale Visualisierung benötigt Matplotlib, das bereits in der
repositoryweiten `requirements.txt` enthalten ist:

```bash
python -m pip install -r requirements.txt
python examples/06_robotics/inverse_kinematics_2d/draw_robot.py
```

Das Skript öffnet das Diagramm und speichert es als `robot_kinematics.png`
im Beispielordner. Ändere den Aufruf `zeichne_roboter(100.0, 120.0)` am
Skriptende, um andere Zielpunkte zu zeigen. Für unerreichbare Ziele löst
die Zeichenfunktion `ValueError` aus, da keine Armstellung gezeichnet werden kann.
Die Berechnungsfunktion liefert weiterhin `None`.

Die gestrichelte Verlängerung des ersten Arms zeigt, wo der relative Winkel
`beta` beginnt. Er ist nicht der Innenwinkel des Armdreiecks.
Beide Achsen haben den gleichen Maßstab, damit Längen und Winkel korrekt erscheinen.
Zum Speichern ohne Fenster in PowerShell:

```powershell
$env:MPLBACKEND = "Agg"
python examples/06_robotics/inverse_kinematics_2d/draw_robot.py
```

### Lösung mit Maxima

Optional wird Maxima oder wxMaxima benötigt; die Python-Beispiele sind davon unabhängig.
Öffne eine Maxima-Sitzung im Beispielordner und führe aus:

```maxima
r: sqrt(100^2 + 120^2)$
gamma: atan2(120, 100)$
batch("solution.mac");
```

Alternativ vom Repository-Hauptordner in einer Maxima-Sitzung mit bereits
gesetzten Variablen `r` und `gamma`:

```maxima
batch("examples/06_robotics/inverse_kinematics_2d/solution.mac");
```

Die Datei rechnet ohne Funktionsdefinitionen und ohne `block` der Reihe nach:
Innenwinkel am Gelenk, `beta`, Innenwinkel an der Basis und `alpha`.
Sie verwendet dieselben festen Armlängen wie Python. Die Erreichbarkeitsprüfung
erfolgt außerhalb der Maxima-Lösung.
Der Zielpunkt ist durch `r` (Abstand in mm) und `gamma` (Zielrichtung im Bogenmaß)
gegeben. Diese Variablen müssen vor dem Laden gesetzt sein und werden nicht
überschrieben. `gamma` entspricht hier dem Winkel `theta` im Diagramm;
der Innenwinkel am Gelenk wird in der Maxima-Datei anders benannt.
Eine Zielrichtung in Grad muss vorher mit `gamma: winkel_grad*%pi/180$`
umgerechnet werden. Die Ergebniswinkel werden in `alpha` und `beta` in Grad
abgelegt und angezeigt: beispielsweise ungefähr `alpha = 23.862` und
`beta = 60.0` für den Zielpunkt `(100, 120)`.
Falls `x` und `y` gegeben sind, berechne vor dem Laden:

```maxima
r: sqrt(x^2 + y^2)$
gamma: atan2(y, x)$
```

Endliche reelle Eingaben und erreichbare Zielpunkte werden vorausgesetzt.

Die Befehle sind im [Maxima-Handbuch](https://maxima.sourceforge.io/docs/manual/maxima_singlepage.html)
dokumentiert.

### Didaktische Hinweise

Die Schnittstelle bleibt auf `x, y` beschränkt; die Robotergeometrie steht in
`ARM_1_MM` und `ARM_2_MM`. Beim Ändern der Armlängen müssen auch die Testdaten
und die dokumentierten Arbeitsbereichsgrenzen angepasst werden.

Im Inneren des Arbeitsbereichs gibt es gewöhnlich zwei Gelenkkonfigurationen.
Die Aufgabe wählt eindeutig die mit positivem `beta`. Als Erweiterung können
Lernende die zweite Lösung mit negativem `beta` berechnen und vergleichen.
`alpha` wird nicht auf den Bereich von 0° bis 360° normiert.

Zur Überprüfung dienen die Gleichungen der Vorwärtskinematik:

$$
x = l_1\cos\alpha + l_2\cos(\alpha+\beta), \qquad
y = l_1\sin\alpha + l_2\sin(\alpha+\beta)
$$

Besprecht, weshalb Punkte nahe am Ursprung bei unterschiedlich langen Armen
unerreichbar sind und weshalb die Tests `assertAlmostEqual()` verwenden.
