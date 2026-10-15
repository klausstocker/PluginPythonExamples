"""Die Ausgabe fuer die Werte aus dataset.py pruefen."""

import unittest

import dataset
from common import RedirectedStdout


def correct_implementation():
    """Die Dauer einer festgelegten Versuchsreihe aufsummieren."""
    anzahl = int(dataset.anzahl.value)
    startdauer = float(dataset.startdauer.value)
    zuwachs = float(dataset.zuwachs.value)
    gesamtdauer = 0.0
    dauer = startdauer
    for versuch in range(anzahl):
        gesamtdauer = gesamtdauer + dauer
        dauer = dauer + zuwachs
    print(f'Gesamtdauer: {gesamtdauer:.1f} s')



class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_output(self):
        with RedirectedStdout() as student_out:
            import answer
        with RedirectedStdout() as expected_out:
            correct_implementation()
        self.assertEqual(str(student_out), str(expected_out))


if __name__ == "__main__":
    unittest.main()
