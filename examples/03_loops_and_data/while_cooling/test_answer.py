"""Die Ausgabe für die Werte aus dataset.py prüfen."""

import unittest

import dataset
from common import RedirectedStdout


def correct_implementation():
    """Mit einer Zustandsfunktion eine Zieltemperatur erreichen."""

    def abkuehlen(temperatur: float, umgebung: float) -> float:
        return (temperatur + umgebung) / 2
    temperatur = float(dataset.temperatur.value)
    umgebung = float(dataset.umgebung.value)
    ziel = float(dataset.ziel.value)
    schritte = 0
    while temperatur > ziel:
        temperatur = abkuehlen(temperatur, umgebung)
        schritte = schritte + 1
    print(f'Schritte: {schritte}')
    print(f'Temperatur: {temperatur:.2f} °C')


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_output(self):
        with RedirectedStdout() as student_out:
            import answer
        with RedirectedStdout() as expected_out:
            correct_implementation()
        self.assertEqual(str(student_out), str(expected_out))


if __name__ == "__main__":
    unittest.main()
