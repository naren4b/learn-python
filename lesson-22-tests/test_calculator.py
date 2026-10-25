"""Run: python -m unittest discover -s lesson-22-tests -p 'test_*.py' -v"""

import unittest
from importlib.machinery import SourceFileLoader
from pathlib import Path

# The lesson reference filename starts with a digit, so load by path.
module = SourceFileLoader(
    "calculator", str(Path(__file__).with_name("22_calculator.py"))
).load_module()


class TestCalculateTotal(unittest.TestCase):
    def test_regular_order(self):
        self.assertEqual(module.calculate_total(12, 2), 24)

    def test_zero_quantity(self):
        self.assertEqual(module.calculate_total(12, 0), 0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            module.calculate_total(12, -1)


if __name__ == "__main__":
    unittest.main()
