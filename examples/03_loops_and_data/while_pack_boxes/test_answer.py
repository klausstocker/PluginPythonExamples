"""Die Ausgabe für die Werte aus dataset.py prüfen."""

import unittest

import dataset
from common import RedirectedStdout


def correct_implementation():
    """Vollständige Kartons durch wiederholtes Abziehen zählen."""
    bestand = int(dataset.bestand.value)
    kartongroesse = int(dataset.kartongroesse.value)
    kartons = 0
    while bestand >= kartongroesse:
        bestand = bestand - kartongroesse
        kartons = kartons + 1
    print(f'Kartons: {kartons}')
    print(f'Rest: {bestand}')


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_output(self):
        with RedirectedStdout() as student_out:
            import answer
        with RedirectedStdout() as expected_out:
            correct_implementation()
        self.assertEqual(str(student_out), str(expected_out))


if __name__ == "__main__":
    unittest.main()
