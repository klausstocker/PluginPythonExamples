"""Teste denselben Auswertungscode mit ausgetauschten Eingabewerten."""

import contextlib
import io
from pathlib import Path
import unittest


class Checker(unittest.TestCase):
    def test_input_cases(self):
        # Eingaben stehen vor der Markierung; der Lösungscode danach bleibt unverändert.
        source = Path(__file__).with_name("answer.py").read_text(encoding="utf-8")
        calculation = source.split("# Auswertung", 1)[1]
        cases = [({'spannung': 209.9}, False), ({'spannung': 210.0}, True), ({'spannung': 225.0}, True), ({'spannung': 250.0}, True), ({'spannung': 250.1}, False)]
        for inputs, expected in cases:
            with self.subTest(inputs=inputs):
                values = inputs.copy()
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(calculation, values)
                self.assertIs(values["spannung_erlaubt"], expected)


if __name__ == "__main__":
    unittest.main()
