# Day 11: Functions, arguments and scope

## Objective
Refresh function parameters, return values, default and keyword arguments, `*args`, `**kwargs`, lambdas and local scope.

## Key concepts
- `def function(parameter):` creates a reusable function; `return` gives a result to the caller.
- Default arguments provide optional inputs: `def total(price, quantity=1):`.
- Keyword arguments clarify meaning: `total(price=100, quantity=2)`.
- `*args` receives extra positional arguments as a tuple.
- `**kwargs` receives extra named arguments as a dictionary.
- Function-local variables do not automatically become globals.
- `lambda x: x * 2` is a small anonymous function.
- Optional type annotations: `def total(x: int) -> int:`; Python doesn't enforce them at runtime.

## Practical example
```python
def total_price(price, quantity=1):
    return price * quantity

print(total_price(50, quantity=3))
```

## Important trade-offs
Prefer explicit parameters for normal APIs. Use `*args` or `**kwargs` only when a variable number of inputs is needed. A `return` value can be reused or tested; `print` merely displays a value. Avoid mutable default parameters such as `items=[]`.

## Reference
Run `python day-11/11_functions.py` from the repo root.

Expected:
```text
Total: 300.00
Labels: 3
Region: eu-central-1
Double: 8
```

Use [diy.md](diy.md) for independent practice; root [diy.sh](../diy.sh) prepares ignored `lab/app.py`. No external dependencies.
