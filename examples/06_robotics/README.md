# 6. Robotik

Selbstständige Beispiele zu Berechnungen und Bewegungen von Robotern.

## Beispiele

1. [Inverse Kinematik eines planaren Zweiachsroboters](inverse_kinematics_2d/README.md): Aus einer Zielposition `(x, y)` die Gelenkwinkel `(alpha, beta)` berechnen.
2. [Vorwärtskinematik eines planaren RTR-Roboters](forward_kinematics_rtr/README.md): Aus Basiswinkel, Ausfahrweg und Handgelenkwinkel die TCP-Position und Greiferorientierung berechnen.
3. [Vorwärtskinematik eines planaren Zweiachsroboters](forward_kinematics_2d/README.md): Aus den beiden Gelenkwinkeln die Endpunktposition `(x, y)` berechnen.
4. [Inverse Kinematik eines planaren RTR-Roboters](inverse_kinematics_rtr/README.md): Aus TCP-Position und Greiferorientierung den Basiswinkel, Ausfahrweg und Handgelenkwinkel berechnen.

## Tests

Die Testbefehle stehen im jeweiligen Beispiel-README. Alle Beispiele:

```bash
python -m unittest test_all_examples.py
```

Für dieses Kapitel reicht Python 3.10 oder neuer mit der Standardbibliothek.
