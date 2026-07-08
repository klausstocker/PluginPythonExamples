"""Run every example test suite in its own example directory.

Each example keeps a standalone `import answer` so it can be copied to or run in
another environment. This repository-level runner executes every example in a
separate Python process with that example folder as the working directory, which
avoids module-name collisions between multiple `answer.py` files.
"""

import subprocess
import sys
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).parent
EXAMPLES_ROOT = REPOSITORY_ROOT / "examples"


def example_directories():
    """Return example folders that contain a unittest file."""
    return sorted(
        example_path
        for example_path in EXAMPLES_ROOT.iterdir()
        if example_path.is_dir() and (example_path / "test_answer.py").exists()
    )


class ExampleTestSuites(unittest.TestCase):
    """Run each self-contained example test suite."""

    def test_examples_can_run_standalone(self):
        for example_path in example_directories():
            with self.subTest(example=example_path.name):
                completed_process = subprocess.run(
                    [sys.executable, "-m", "unittest", "test_answer.py"],
                    cwd=example_path,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                output = completed_process.stdout + completed_process.stderr
                self.assertEqual(completed_process.returncode, 0, output)


if __name__ == "__main__":
    unittest.main()
