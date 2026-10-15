"""Die Ausgabe für die Werte aus dataset.py prüfen."""

import unittest

import dataset
from common import RedirectedStdout


def correct_implementation():
    """Einen Füllstand erhöhen, bis das Ziel erreicht ist."""
    fuellstand = float(dataset.fuellstand.value)
    ziel = float(dataset.ziel.value)
    zufluss = float(dataset.zufluss.value)
    schritte = 0
    while fuellstand < ziel:
        fuellstand = fuellstand + zufluss
        schritte = schritte + 1
    print(f'Schritte: {schritte}')
    print(f'Füllstand: {fuellstand:.1f} l')


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_output(self):
        with RedirectedStdout() as student_out:
            import answer
        with RedirectedStdout() as expected_out:
            correct_implementation()
        self.assertEqual(str(student_out), str(expected_out))


if __name__ == "__main__":
    unittest.main()
