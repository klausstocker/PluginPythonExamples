# Inverse Kinematik eines planaren RTR-Roboters

## Lernziel

Aus einer gewünschten TCP-Position und Greiferorientierung die Gelenkwerte
eines RTR-Roboters berechnen. Einen gedrehten Werkzeugversatz zurückrechnen,
`atan2()` für alle Quadranten verwenden und die Erreichbarkeit einer Pose prüfen.

## Aufgabe

Der Roboter entspricht „Example 4: an RTR planar robot reaches a circle“ im
[Robotik-Skript](../../../Robotics_Script.md) und dem Beispiel zur
[RTR-Vorwärtskinematik](../forward_kinematics_rtr/README.md).
Alle erforderlichen Geometrieangaben stehen auch hier.
Schreibe folgende Funktion:

```python
def inverse_kinematics(
    x: float, y: float, phi: float
) -> tuple[float, float, float] | None:
    ...
```

Die Eingaben sind die gewünschte TCP-Position `(x, y)` in Millimetern und
die absolute Greiferorientierung `phi` in Grad. Die Funktion gibt
`(r1, d, r2)` zurück: Basiswinkel in Grad, Ausfahrweg in Millimetern und
relativer Handgelenkwinkel in Grad. Runde innerhalb der Funktion nicht
und gib dort nichts aus. Bei nicht endlichen Eingaben (`nan`, `inf`, `-inf`)
oder einer unerreichbaren Pose liefert sie `None`.

Es gelten folgende Konventionen:

- Die Basis liegt im Ursprung. Die positive Welt-x-Achse zeigt nach rechts,
  die positive Welt-y-Achse nach oben. Positive Winkel drehen gegen den Uhrzeigersinn.
- `r1` dreht den Arm relativ zur Welt-x-Achse. `d` verschiebt das Handgelenk
  entlang der gedrehten lokalen x-Achse des Arms. Es gibt keine feste Armlänge.
- Der Ausfahrweg liegt zwischen 0 und 7 mm einschließlich.
- `r2` dreht den Greifer relativ zum Arm. Die Orientierung seiner lokalen
  x-Achse ist `phi = r1 + r2`. Beide Drehgelenke können frei drehen;
  Kollisionen werden nicht betrachtet.
- Der TCP liegt vom Handgelenk aus um `a = 0.9` mm entlang der lokalen
  **positiven y-Achse des Greifers** versetzt.
- Verwende für `r1` den von `math.atan2()` gelieferten Winkel im Bereich
  von −180° bis 180°. Berechne `r2 = phi - r1` ohne weitere Normierung.
- Liegt das Handgelenk im Ursprung, ist die Armrichtung unbestimmt.
  Wähle dann eindeutig `r1 = 0°`, `d = 0` und `r2 = phi`.

Die Vorwärtsbeziehungen lauten:

$$
\begin{aligned}
\varphi &= r_1+r_2,\\
x &= d\cos r_1 - a\sin\varphi,\\
y &= d\sin r_1 + a\cos\varphi.
\end{aligned}
$$

1. Prüfe mit `math.isfinite()`, ob alle Eingaben endlich sind.
2. Wandle `phi` mit `math.radians()` ins Bogenmaß um. Berechne den gedrehten
   TCP-Versatz und ziehe ihn von der Zielposition ab. So erhältst du
   die Handgelenkkoordinaten `(wrist_x, wrist_y)`.
3. Berechne den Ausfahrweg mit `math.hypot(wrist_x, wrist_y)` und prüfe,
   ob das Handgelenk erreichbar ist. Entscheidend ist dessen Abstand,
   nicht der Abstand des TCP zum Ursprung.
4. Bestimme die Basisrichtung mit `math.atan2(wrist_y, wrist_x)` und wandle
   sie mit `math.degrees()` in Grad um. Behandle den Ursprung gesondert.
5. Bestimme den relativen Handgelenkwinkel und gib alle drei Werte als Tupel zurück.

Verwende eine absolute Längentoleranz von `1e-12` mm für Rundungsfehler:
Bei `d <= 1e-12` behandle das Handgelenk als Ursprung. Liegt `d` höchstens
um diese Toleranz über 7 mm, setze es auf 7 mm; größere Werte sind unerreichbar.
Mit `math.isclose()` muss dabei `rel_tol=0.0` gesetzt werden.

Beispiel: `inverse_kinematics(4.0, 3.0, 90.0)` liefert ungefähr
`(31.476839350, 5.745432969, 58.523160650)`.
Das Handgelenk liegt dabei bei `(4.9, 3.0)` mm.

## Dateien

- `answer.py` enthält die Musterlösung mit Geometriekonstanten und Beispielaufruf.
- `test_answer.py` prüft Ziele in allen Quadranten, unterschiedliche
  Orientierungen am selben Ziel, Ausfahrgrenzen, den Ursprung und ungültige Eingaben.
  Die unabhängige Hilfsfunktion `forward_pose()` prüft durch schrittweise
  Vorwärtstransformation, ob die berechneten Gelenkwerte die Zielpose erreichen.

## Voraussetzungen

Python 3.10 oder neuer, nur Standardbibliothek (`math` und `unittest`).
Grundkenntnisse zu Funktionen, Tupeln, Winkelfunktionen und 2D-Rotationen.
Die Eingaben sind Zahlen; andere Datentypen werden nicht geprüft.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/06_robotics/inverse_kinematics_rtr/answer.py
python -m unittest discover -s examples/06_robotics/inverse_kinematics_rtr -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Gib den Lernenden die Aufgabenbeschreibung und die Tests; `answer.py` dient
als Musterlösung. Als Start genügt die Funktionssignatur mit `pass` und ein
Import von `math`. Beim Ändern der Geometrie müssen Konstanten, Testdaten
und Aufgabenbeschreibung gemeinsam angepasst werden.

Die Testwerte unterscheiden sich vom Beispielaufruf. Besprecht, weshalb eine
TCP-Position erst zusammen mit ihrer Orientierung die Gelenkwerte festlegt.
Ein TCP kann mehr als 7 mm vom Ursprung entfernt sein und trotzdem erreichbar
sein. Umgekehrt kann ein näherer TCP bei ungünstiger Orientierung unerreichbar sein.

Bei `d = 0` können beliebig viele Kombinationen von `r1` und `r2` dieselbe Pose
erzeugen. Die festgelegte Wahl macht die Rückgabe eindeutig.
Die Längentoleranz behandelt numerische Rundungsfehler; sie modelliert keine
mechanische Toleranz. `assertAlmostEqual()` berücksichtigt Gleitkommafehler
beim Vergleich der rekonstruierten Pose.

Als Erweiterung können Lernende die beiden RTR-Beispiele kombinieren und die
Vorwärtskinematik auf die berechneten Gelenkwerte anwenden. Verglichen werden
die Zielposition und die absolute Orientierung.
