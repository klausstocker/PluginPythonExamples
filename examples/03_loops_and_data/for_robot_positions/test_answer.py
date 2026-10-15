"""Die Ausgabe fuer die Werte aus dataset.py pruefen."""

import unittest

import dataset
from common import RedirectedStdout


def correct_implementation():
    """Positionen nach gleich großen Verfahrwegen berechnen."""
    anzahl = int(dataset.anzahl.value)
    schrittweite = float(dataset.schrittweite.value)
    for schritt in range(1, anzahl + 1):
        position = schritt * schrittweite
        print(f'Schritt {schritt}: {position:.1f} mm')



class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_output(self):
        with RedirectedStdout() as student_out:
            import answer
        with RedirectedStdout() as expected_out:
            correct_implementation()
        self.assertEqual(str(student_out), str(expected_out))


if __name__ == "__main__":
    unittest.main()
