"""Die Ausgabe für die Werte aus dataset.py prüfen."""

import unittest

import dataset
from common import RedirectedStdout


def correct_implementation():
    """Die Ziffern einer Teilenummer von rechts nach links addieren."""
    teilenummer = int(dataset.teilenummer.value)
    rest = teilenummer
    quersumme = 0
    while rest > 0:
        letzte_ziffer = rest % 10
        quersumme = quersumme + letzte_ziffer
        rest = rest // 10
    print(f'Quersumme: {quersumme}')


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_output(self):
        with RedirectedStdout() as student_out:
            import answer
        with RedirectedStdout() as expected_out:
            correct_implementation()
        self.assertEqual(str(student_out), str(expected_out))


if __name__ == "__main__":
    unittest.main()
