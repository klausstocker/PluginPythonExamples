"""Unit test template for a new plugin example.

After copying this folder into examples/example_name, run from the repository root with:
    python -m unittest discover -s examples/example_name -p "test_*.py"

Before running, replace `examples.example_name` below with your real example package path.
"""

import unittest

from examples.example_name import answer


class Checker(unittest.TestCase):  # do not rename; plugin checks expect this name
    def test_example_function_returns_value(self):
        self.assertEqual(answer.example_function("test value"), "test value")

    def test_example_data_can_be_changed(self):
        self.assertNotEqual(answer.EXAMPLE_VALUE, "test value")


if __name__ == "__main__":
    unittest.main()
