"""Die Ausgabe für die Werte aus dataset.py prüfen."""

import unittest

import dataset
from common import RedirectedStdout


def correct_implementation():
    """Eine Dicke durch wiederholte Funktionsaufrufe verdoppeln."""

    def doppelte_dicke(dicke: float) -> float:
        return dicke * 2
    dicke = float(dataset.dicke.value)
    ziel = float(dataset.ziel.value)
    faltungen = 0
    while dicke < ziel:
        dicke = doppelte_dicke(dicke)
        faltungen = faltungen + 1
    print(f'Faltungen: {faltungen}')
    print(f'Dicke: {dicke:.3f} mm')


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_output(self):
        with RedirectedStdout() as student_out:
            import answer
        with RedirectedStdout() as expected_out:
            correct_implementation()
        self.assertEqual(str(student_out), str(expected_out))


if __name__ == "__main__":
    unittest.main()
