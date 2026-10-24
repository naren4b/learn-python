# Day 4: Functions and return values

## Objective
Write reusable functions with parameters and return values.

## Concept
A function groups reusable logic. Define one with `def`, supply inputs as parameters, and send a result back with `return`. Calling a function executes its body.

## Syntax
```python
def add(a, b):
    return a + b

total = add(2, 3)
print(total)
```

## Important points
- Function names should explain what they do.
- Parameters receive values from the caller.
- `return` gives the result to the caller; `print` only displays it.
- A function without an explicit `return` returns `None`.
- Indent the body four spaces.

## Trade-offs
Choose small functions when logic is reused or easier to test in isolation. Avoid many tiny functions for trivial one-off expressions.

## Practice
Follow [diy.md](diy.md), writing your code in the ignored `lab/app.py`. Reference solution: [04_functions.py](04_functions.py).

Run the maintained example from the repository root:
```bash
python day-4/04_functions.py
```

Expected output:
```text
Unit price after discount: 160.00
Order total: 320.00
In stock: True
```

Only the Python standard library is used.

## Important line notes

- `return` makes function output available to callers; `in_stock` returns a boolean comparison.
