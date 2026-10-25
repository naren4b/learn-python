"""Tests for the lesson's numbered reference file."""

import runpy
import unittest
from pathlib import Path

# runpy loads definitions without requiring a module name starting with a digit.
calculate_total = runpy.run_path(
    str(Path(__file__).with_name("22_calculator.py"))
)["calculate_total"]


class TestCalculateTotal(unittest.TestCase):
    def test_regular_order(self):
        self.assertEqual(calculate_total(12, 2), 24)

    def test_zero_quantity(self):
        self.assertEqual(calculate_total(12, 0), 0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_total(12, -1)


if __name__ == "__main__":
    unittest.main()
