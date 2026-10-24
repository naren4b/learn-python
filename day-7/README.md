# Day 7: Python dictionaries

## Goal
Store named values in key-value pairs and safely read, update and iterate over them.

## Concepts
- A dictionary is a mutable mapping: `server = {"name": "api", "cpu": 4}`.
- Keys must be hashable and unique. Values may have different types.
- Read an existing key with `server["name"]`; a missing key raises `KeyError`.
- Use `server.get("region", "unknown")` for a fallback.
- Assign `server["cpu"] = 8` to update or add a key.
- Iterate pairs with `for key, value in server.items():`.

## Example
```python
server = {"name": "api", "cpu": 4}
server["cpu"] = 8
print(server.get("region", "unknown"))
```

## Trade-offs
Dictionaries are useful for fast lookups by key; lists are better for sequences indexed by position. Dictionary insertion order is preserved in modern Python.

## Reference
Run from the repository root:
```bash
python day-7/07_dictionaries.py
```

Expected:
```text
Server: api
CPU: 8
Region: unknown
name: api
cpu: 8
```

Practice independently with [diy.md](diy.md) and root [diy.sh](../diy.sh). No third-party dependencies.

## Learner questions: values, missing keys and conversion

- Use `server["name"]` or `server.get("name")`; `server("name")` attempts to call a dictionary and raises `TypeError`.
- Store numeric CPU counts as integers when possible. If data arrives as numeric text, `int(server["cpu"])` converts it before comparison; invalid text raises `ValueError`.
- Python's missing-value sentinel is `None`, not JSON's `null`.
- Guard an optional value before conversion: `cpu = server.get("cpu"); if cpu is not None and int(cpu) < 10: ...`. The right-hand side of `and` is skipped when the left side is false.
- `get()` also returns `None` for a present key holding `None`, unless a different fallback is specified.
