"""Unit test template for a new plugin example.

Run from this directory with:
    python -m unittest test_answer.py

Or run from the repository root after copying this folder into examples/ with:
    python -m unittest discover -s examples/example_name -p "test_*.py"
"""

import unittest
import importlib.util
from pathlib import Path


def load_answer_module():
    module_path = Path(__file__).with_name("answer.py")
    spec = importlib.util.spec_from_file_location(
        f"{Path(__file__).parent.name}_answer",
        module_path,
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


answer = load_answer_module()


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_example_function_returns_value(self):
        self.assertEqual(answer.example_function("test value"), "test value")

    def test_example_data_can_be_changed(self):
        self.assertNotEqual(answer.EXAMPLE_VALUE, "test value")


if __name__ == "__main__":
    unittest.main()
