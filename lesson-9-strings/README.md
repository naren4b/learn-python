# Day 9: Working with strings

## Objective
Extract, clean, split and join text in Python.

## Key concepts
- Strings are immutable sequences of characters.
- Indexing: `text[0]` is the first character; `text[-1]` is the last.
- Slicing: `text[start:stop]` excludes `stop`.
- `strip()` removes surrounding whitespace.
- `lower()` and `upper()` change letter case in a new string.
- `split(separator)` creates a list; `join(parts)` combines text.
- `replace(old, new)` returns a modified string.
- `in` checks for a substring.

## Example
```python
text = "  API,DB,Cache  "
clean = text.strip()
services = clean.split(",")
print(services[0])
print(" | ".join(services))
```

## Important trade-offs
String methods do not edit the original string. Assign the returned value when you need to keep it. A missing substring gives `-1` with `find()`; use `in` for simple membership checks.

## Reference
From the repository root:
```bash
python lesson-9-strings/09_strings.py
```

Expected:
```text
First: api
Last: cache
Count: 3
Joined: api | db | cache
Has db: True
```

Practice instructions: [diy.md](diy.md). Reset your ignored local practice files with root [diy.sh](../diy.sh). No extra packages.

## Practice review

The learner split a comma-separated string into a list, counted items, appended a name, accessed the first entry, and joined values with a separator. Avoid naming a variable `str` because it shadows the built-in. Using `{value}` outside an f-string builds a set rather than formatting text. Reuse an already computed `names` list rather than repeatedly splitting. Python 3.12 allows reuse of matching quote styles inside f-string expressions.

## Important line notes

- `strip()` trims edges, `lower()` normalizes case, `split(',')` builds a list, and `join()` combines it.
