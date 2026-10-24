# Day 3: Operators

## Objective
Practice arithmetic, comparison and logical operators.

## Key points
- Arithmetic: `+ - * / // % **`
- Comparisons: `== != > < >= <=`
- Logical: `and or not`
- `=` assigns, `==` compares.
- `/` divides; `//` rounds the quotient down; `%` gives the remainder.

## Example
```python
price = 100
discount = 20
final_price = price - price * discount / 100
print(f"Final price: {final_price:.2f}")
```

## Trade-off
Use `and` when both conditions must be true. Use `or` when either condition is enough.

## Run reference
```bash
python day-3/03_operators.py
```

Or use isolated Podman:
```bash
podman run --rm -v "$PWD:/work" -w /work docker.io/library/python:3.12.14-slim-bookworm python day-3/03_operators.py
```

Expected:
```text
Final price: 80.00
Discount allowed: True
Even number: False
Remainder: 1
```

Follow [diy.md](diy.md). No external dependencies.
