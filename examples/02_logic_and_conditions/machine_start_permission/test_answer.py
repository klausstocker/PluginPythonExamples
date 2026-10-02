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
        cases = [({'tuer_geschlossen': False, 'stoppsignal_aktiv': False, 'taster_links': False, 'taster_rechts': False}, False), ({'tuer_geschlossen': False, 'stoppsignal_aktiv': False, 'taster_links': False, 'taster_rechts': True}, False), ({'tuer_geschlossen': False, 'stoppsignal_aktiv': False, 'taster_links': True, 'taster_rechts': False}, False), ({'tuer_geschlossen': False, 'stoppsignal_aktiv': False, 'taster_links': True, 'taster_rechts': True}, False), ({'tuer_geschlossen': False, 'stoppsignal_aktiv': True, 'taster_links': False, 'taster_rechts': False}, False), ({'tuer_geschlossen': False, 'stoppsignal_aktiv': True, 'taster_links': False, 'taster_rechts': True}, False), ({'tuer_geschlossen': False, 'stoppsignal_aktiv': True, 'taster_links': True, 'taster_rechts': False}, False), ({'tuer_geschlossen': False, 'stoppsignal_aktiv': True, 'taster_links': True, 'taster_rechts': True}, False), ({'tuer_geschlossen': True, 'stoppsignal_aktiv': False, 'taster_links': False, 'taster_rechts': False}, False), ({'tuer_geschlossen': True, 'stoppsignal_aktiv': False, 'taster_links': False, 'taster_rechts': True}, True), ({'tuer_geschlossen': True, 'stoppsignal_aktiv': False, 'taster_links': True, 'taster_rechts': False}, True), ({'tuer_geschlossen': True, 'stoppsignal_aktiv': False, 'taster_links': True, 'taster_rechts': True}, True), ({'tuer_geschlossen': True, 'stoppsignal_aktiv': True, 'taster_links': False, 'taster_rechts': False}, False), ({'tuer_geschlossen': True, 'stoppsignal_aktiv': True, 'taster_links': False, 'taster_rechts': True}, False), ({'tuer_geschlossen': True, 'stoppsignal_aktiv': True, 'taster_links': True, 'taster_rechts': False}, False), ({'tuer_geschlossen': True, 'stoppsignal_aktiv': True, 'taster_links': True, 'taster_rechts': True}, False)]
        for inputs, expected in cases:
            with self.subTest(inputs=inputs):
                values = inputs.copy()
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(calculation, values)
                self.assertIs(values["startfreigabe"], expected)


if __name__ == "__main__":
    unittest.main()
