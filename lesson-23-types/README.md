# Lesson 23 — Type hints and clean code

## Goal
Add readable type annotations and understand what they do (and do not) enforce.

## Common annotations

| Example | Meaning |
| --- | --- |
| `name: str` | String parameter |
| `port: int = 8080` | Integer with default |
| `-> bool` | Function intended to return a boolean |
| `list[str]` | List of strings |
| `dict[str, int]` | Dictionary with string keys and integer values |
| `str | None` | Optional string (Python 3.10+) |

## Example

```python
def format_service(name: str, port: int = 8080) -> str:
    return f"{name}:{port}"
```

**Important:** Python annotations do not normally validate argument types at runtime. A static type checker, such as mypy or Pyright, can flag mismatches before execution.

## Clean-code habits

- Use descriptive `snake_case` names and small functions.
- Return values rather than mixing business logic with `print()`.
- Handle specific exceptions and avoid mutable default arguments.
- Keep comments focused on **why**, rather than repeating obvious code.
- Use `is None` when checking for `None`.

[DIY](diy.md) · [Reference](23_types.py) · [Official typing docs](https://docs.python.org/3.12/library/typing.html) · [PEP 8](https://peps.python.org/pep-0008/)
