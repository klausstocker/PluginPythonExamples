"""Pruefe die Filter und ihre genaue Ausgabe auf stdout."""

import io
import runpy
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import answer


class Checker(unittest.TestCase):
    def test_age_under_ten(self):
        people = [("Mia", 9), ("Jonas", 10), ("Lea", 0), ("Robert", 11)]
        output = io.StringIO()
        with redirect_stdout(output):
            answer.print_names_under_ten(people)
        self.assertEqual(output.getvalue(), "Mia\nLea\n")

    def test_long_name_or_even_age(self):
        # Alle vier Kombinationen sowie die Grenze von fuenf Buchstaben.
        people = [("Sophie", 13), ("Tom", 12), ("Johanna", 14), ("Felix", 15)]
        output = io.StringIO()
        with redirect_stdout(output):
            answer.print_names_long_or_even_age(people)
        self.assertEqual(output.getvalue(), "Sophie\nTom\nJohanna\n")

    def test_empty_list(self):
        output = io.StringIO()
        with redirect_stdout(output):
            answer.print_names_under_ten([])
            answer.print_names_long_or_even_age([])
        self.assertEqual(output.getvalue(), "")

    def test_no_matches(self):
        output = io.StringIO()
        with redirect_stdout(output):
            answer.print_names_under_ten([("Tim", 11)])
            answer.print_names_long_or_even_age([("Tim", 11)])
        self.assertEqual(output.getvalue(), "")

    def test_script_outputs_only_names(self):
        output = io.StringIO()
        with redirect_stdout(output):
            runpy.run_path(str(Path(__file__).with_name("answer.py")), run_name="__main__")
        self.assertEqual(output.getvalue(), "Anna\nDavid\nAnna\nBenjamin\nClara\n")


if __name__ == "__main__":
    unittest.main()
