"""Die Ausgabe fuer die Werte aus dataset.py pruefen."""

import unittest

import dataset
from common import RedirectedStdout


def correct_implementation():
    """Eine Umrechnungsfunktion für alle Tabellenzeilen verwenden."""

    def fahrenheit(celsius: float) -> float:
        return celsius * 9 / 5 + 32
    start = int(dataset.start.value)
    stopp = int(dataset.stopp.value)
    schrittweite = int(dataset.schrittweite.value)
    for celsius in range(start, stopp, schrittweite):
        temperatur_fahrenheit = fahrenheit(celsius)
        print(f'{celsius} °C = {temperatur_fahrenheit:.1f} °F')



class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_output(self):
        with RedirectedStdout() as student_out:
            import answer
        with RedirectedStdout() as expected_out:
            correct_implementation()
        self.assertEqual(str(student_out), str(expected_out))


if __name__ == "__main__":
    unittest.main()
