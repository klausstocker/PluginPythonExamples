# Vorwärtskinematik eines planaren RTR-Roboters

## Lernziel

Eine Funktion mit drei Eingaben und drei Rückgabewerten schreiben. Lokale und
globale Koordinaten unterscheiden, Rotation und Translation in der richtigen
Reihenfolge anwenden und die Position des Tool Centre Point (TCP) berechnen.

Das Beispiel entspricht „Example 4: an RTR planar robot reaches a circle“ im
[Robotik-Skript](../../../Robotics_Script.md). Alle Angaben zur Geometrie stehen
auch hier, damit der Beispielordner unabhängig vom Skript verwendet werden kann.

## Aufgabe

Ein RTR-Roboter bewegt sich in der xy-Ebene. RTR steht für
Rotation–Translation–Rotation. Schreibe folgende Funktion:

```python
def forward_kinematics(
    r1: float, d: float, r2: float
) -> tuple[float, float, float] | None:
    ...
```

Die Eingaben sind der Basiswinkel `r1` in Grad, der Ausfahrweg `d` in Millimetern
und der relative Handgelenkwinkel `r2` in Grad. Die Funktion gibt
`(x, y, phi)` zurück: die TCP-Position im Weltkoordinatensystem in Millimetern
und die absolute Greiferorientierung in Grad. Runde innerhalb der Funktion
nicht und gib dort nichts mit `print()` aus.

Es gelten folgende Konventionen:

- Die Basis liegt im Ursprung; die positive x-Achse zeigt nach rechts,
  die positive y-Achse nach oben. Positive Winkel drehen gegen den Uhrzeigersinn.
- `r1` dreht den Arm relativ zur positiven Welt-x-Achse.
- `d` verschiebt das Handgelenk entlang der bereits gedrehten lokalen x-Achse
  des Arms. Es gibt keine zusätzliche feste Armlänge. Es gilt `0 <= d <= 7` mm.
- `r2` dreht den Greifer relativ zum Arm. Die Orientierung `phi` bezeichnet
  die lokale x-Achse des Greifers relativ zur Welt-x-Achse.
- Der TCP liegt vom Handgelenk aus um `a = 0.9` mm entlang der lokalen
  **positiven y-Achse des Greifers** versetzt. TCP und Handgelenk sind daher
  unterschiedliche Punkte.
- Beide Drehgelenke können frei drehen. Gib `phi = r1 + r2` ohne Normierung
  auf einen bestimmten Winkelbereich zurück. Kollisionen werden nicht betrachtet.
- Bei nicht endlichen Eingaben (`nan`, `inf`, `-inf`) oder einem Ausfahrweg
  außerhalb des erlaubten Bereichs liefert die Funktion `None`.

1. Prüfe die Eingaben mit `math.isfinite()` und die Grenzen für `d`.
2. Bestimme die absolute Greiferorientierung und rechne die für Sinus und
   Kosinus benötigten Winkel mit `math.radians()` ins Bogenmaß um.
3. Berechne die Handgelenkposition aus Ausfahrweg und Basiswinkel.
4. Drehe den lokalen TCP-Versatz mit der absoluten Greiferorientierung und
   addiere ihn zur Handgelenkposition.
5. Gib die beiden TCP-Koordinaten und die Orientierung als Tupel zurück.

Die mathematischen Beziehungen sind (Winkelfunktionen verwenden Bogenmaß):

$$
\varphi = r_1 + r_2, \qquad
\vec{w} = \begin{bmatrix}d\cos r_1\\d\sin r_1\end{bmatrix}
$$

$$
\vec{p}_{TCP} = \vec{w} +
\begin{bmatrix}\cos\varphi & -\sin\varphi\\
\sin\varphi & \cos\varphi\end{bmatrix}
\begin{bmatrix}0\\0.9\end{bmatrix}.
$$

Leite daraus selbst die Gleichungen für `x` und `y` ab.

Beispiel aus dem Skript:

```python
forward_kinematics(31.476839350, 5.745432969, 58.523160650)
# ungefähr (4.0, 3.0, 90.0)
```

Das Handgelenk liegt dabei ungefähr bei `(4.9, 3.0)` mm. Erst der gedrehte
TCP-Versatz führt zum Greifpunkt `(4.0, 3.0)` mm.

## Dateien

- `answer.py` enthält die Musterlösung mit Geometriekonstanten und Beispielaufruf.
- `test_answer.py` prüft lokale Translation, gedrehten TCP-Versatz, relative
  Handgelenkwinkel, freie Drehwinkel, Ausfahrgrenzen und ungültige Eingaben.
  Die Referenzfunktion `correct()` transformiert den TCP unabhängig in drei
  Schritten: Handgelenkrotation, Armtranslation, Basisrotation.

## Voraussetzungen

Python 3.10 oder neuer, nur Standardbibliothek (`math` und `unittest`).
Grundkenntnisse zu Funktionen, Tupeln, Sinus, Kosinus und 2D-Rotationen.
Die Eingaben sind Zahlen; eine Prüfung anderer Datentypen ist nicht Teil der Aufgabe.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/06_robotics/forward_kinematics_rtr/answer.py
python -m unittest discover -s examples/06_robotics/forward_kinematics_rtr -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Gib den Lernenden die Aufgabenbeschreibung und die Tests; `answer.py` dient als
Musterlösung für Lehrkräfte. Als Start genügt die Funktionssignatur mit `pass`
und ein Import von `math`. Beim Ändern der Geometrie müssen die Konstanten,
die Testdaten und die Aufgabenbeschreibung gemeinsam angepasst werden.

Die Testwerte unterscheiden sich vom Beispielaufruf. Bekannte Achsstellungen
machen Vorzeichenfehler sichtbar; schräge Stellungen prüfen die Verkettung der
Bewegungen. `assertAlmostEqual()` berücksichtigt Rundungsfehler von Gleitkommazahlen.
Auch bei `d = 0` bleibt der TCP um 0.9 mm vom Ursprung entfernt.

Als Erweiterung können Lernende dieselbe Funktion mit homogenen 3×3-Matrizen
und NumPy implementieren. Die Reihenfolge aus dem Skript lautet
`T_WG = R1 @ Tx @ R2`; der lokale TCP ist `[0, 0.9, 1]`.
NumPy steht bereits in der repositoryweiten `requirements.txt` und wird nur
für diese Erweiterung benötigt. Beide Implementierungen sollen dieselben Tests bestehen.
