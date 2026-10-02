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
        cases = [({'handbetrieb': False, 'automatikbetrieb': False}, False), ({'handbetrieb': False, 'automatikbetrieb': True}, True), ({'handbetrieb': True, 'automatikbetrieb': False}, True), ({'handbetrieb': True, 'automatikbetrieb': True}, False)]
        for inputs, expected in cases:
            with self.subTest(inputs=inputs):
                values = inputs.copy()
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(calculation, values)
                self.assertIs(values["genau_eine_betriebsart"], expected)
                self.assertIs(values["mindestens_eine_betriebsart"], inputs["handbetrieb"] or inputs["automatikbetrieb"])


if __name__ == "__main__":
    unittest.main()
