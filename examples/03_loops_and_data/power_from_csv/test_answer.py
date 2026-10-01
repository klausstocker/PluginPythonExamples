"""Check file input and stdout without modifying the supplied measurements."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


EXAMPLE_DIRECTORY = Path(__file__).resolve().parent
ANSWER_PATH = EXAMPLE_DIRECTORY / "answer.py"


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def assert_program_output(self, directory: Path, expected: float) -> None:
        completed = subprocess.run(
            [sys.executable, str(ANSWER_PATH)],
            cwd=directory,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(len(completed.stdout.strip().splitlines()), 1)
        self.assertAlmostEqual(float(completed.stdout.strip()), expected)

    def check_measurements(self, rows: list[str], expected: float) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            (directory / "measurements.csv").write_text(
                "\n".join(rows), encoding="utf-8"
            )
            self.assert_program_output(directory, expected)

    def test_reads_twelfth_row(self):
        rows = ["10;2"] * 10 + ["11;3", "7.5;0.4", "13;5", "14;6"]
        self.check_measurements(rows, 3.0)

    def test_negative_power(self):
        rows = ["8;2"] * 11 + ["-4.5;2", "6;3"]
        self.check_measurements(rows, -9.0)

    def test_two_negative_samples(self):
        rows = ["8;2"] * 11 + ["-3;-0.25", "6;3"]
        self.check_measurements(rows, 0.75)

    def test_zero_current(self):
        rows = ["8;2"] * 11 + ["12;0", "6;3"]
        self.check_measurements(rows, 0.0)

    def test_exactly_twelve_rows_without_final_newline(self):
        rows = ["8;2"] * 11 + ["2.5;1.2"]
        self.check_measurements(rows, 3.0)

    def test_supplied_measurements(self):
        self.assert_program_output(EXAMPLE_DIRECTORY, 1.608908)


if __name__ == "__main__":
    unittest.main()
