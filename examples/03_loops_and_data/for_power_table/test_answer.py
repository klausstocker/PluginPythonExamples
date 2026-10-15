"""Die Ausgabe fuer die Werte aus dataset.py pruefen."""

import unittest

import dataset
from common import RedirectedStdout


def correct_implementation():
    """Für jeden Stromwert die Leistungsfunktion aufrufen."""

    def leistung_watt(spannung: float, strom: float) -> float:
        return spannung * strom
    spannung = float(dataset.spannung.value)
    start = int(dataset.start.value)
    stopp = int(dataset.stopp.value)
    schrittweite = int(dataset.schrittweite.value)
    for strom in range(start, stopp, schrittweite):
        leistung = leistung_watt(spannung, strom)
        print(f'I = {strom} A: {leistung:.1f} W')



class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_output(self):
        with RedirectedStdout() as student_out:
            import answer
        with RedirectedStdout() as expected_out:
            correct_implementation()
        self.assertEqual(str(student_out), str(expected_out))


if __name__ == "__main__":
    unittest.main()
