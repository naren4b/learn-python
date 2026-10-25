# Lesson 22 — Unit testing with unittest

## Goal

Write automated checks for Python functions using the built-in `unittest` framework.

## Example

```python
import unittest

def calculate_total(price, quantity):
    return price * quantity

class TestCalculateTotal(unittest.TestCase):
    def test_valid_quantity(self):
        self.assertEqual(calculate_total(10, 2), 20)

if __name__ == "__main__":
    unittest.main()
```

## Key concepts

| Item | Meaning |
| --- | --- |
| `unittest.TestCase` | Base class for test cases |
| `test_...` | Test method discovered automatically |
| `self.assertEqual(actual, expected)` | Compare output |
| `self.assertRaises(ValueError)` | Verify an expected error |
| `setUp()` | Initialize before each test |
| `python -m unittest discover` | Find and run tests |

Separate business logic from CLI/network calls so tests stay fast and repeatable. Do not use live APIs in unit tests; mock dependencies when necessary.

## Run

```bash
python -m unittest discover -s lesson-22-tests -p 'test_*.py' -v
```

[DIY](diy.md) · [Implementation](22_calculator.py) · [Unit tests](test_calculator.py) · [Official unittest docs](https://docs.python.org/3.12/library/unittest.html).
