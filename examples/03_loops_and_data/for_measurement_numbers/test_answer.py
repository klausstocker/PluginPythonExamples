"""Die Ausgabe fuer den in dataset.py hinterlegten Wert pruefen."""

import unittest

import dataset
from common import RedirectedStdout


def correct_implementation():
    """Eine vorgegebene Anzahl von Messungen nummerieren."""
    anzahl = int(dataset.a.value)
    for index in range(anzahl):
        print(f'Messung {index + 1}')
    print('Fertig.')



class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_output(self):
        with RedirectedStdout() as student_out:
            import answer
        with RedirectedStdout() as expected_out:
            correct_implementation()
        self.assertEqual(str(student_out), str(expected_out))


if __name__ == "__main__":
    unittest.main()
