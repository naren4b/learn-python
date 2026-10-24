# Day 2: Strings, integers, floats and booleans

## Objective
Create values using Python's four common basic types and print them clearly.

## Concept
A string (`str`) stores text, an integer (`int`) stores whole numbers, a float (`float`) stores decimal numbers, and a boolean (`bool`) stores `True` or `False`. Python determines their types from the assigned values.

## Key points
- Text uses quotes: `city = "Chennai"`.
- Whole number: `count = 3`; decimal: `price = 12.5`.
- Booleans have capital letters: `active = True`.
- Use `type(value)` to inspect the type and `f"Text: {value}"` to format output.
- `int("45")` converts numeric text to an integer; `str(45)` converts a number to text.

## Trade-offs
- `int` is for exact whole numbers; `float` is for approximate decimal calculations. Do not use `float` for precise money calculations.
- A numeric string such as `"45"` is text, not a number.

## Practice
Follow [diy.md](diy.md), type the solution into your local `app.py`, and run it in WSL. Check the types using `type()`. Change an integer to a numeric string and observe how its type changes.

## Run the reference in WSL
```bash
python day-2/02_types.py
```

## Isolated Podman
```bash
podman run --rm -v "$PWD:/work" -w /work \
  docker.io/library/python:3.12.14-slim-bookworm \
  python day-2/02_types.py
```

## Expected output
```text
Chennai: str
45: int
12.5: float
True: bool
Next year: 46
```

No external dependencies.

## Notes from practice

- `type(value).__name__` prints readable type names such as `str`, `float` and `bool`.
- Keep postal codes as strings, because they are identifiers, not quantities.
- An f-string starts with `f`; expressions inside `{...}` are evaluated. For example, `f"{price:.2f}"` displays a decimal with two digits after the point.
- To calculate a 20% discount, use `price * 20 / 100`. The `%` operator means remainder: `10 % 3` is `1`.
