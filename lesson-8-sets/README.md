# Day 8: Tuples and sets

## Objective
Choose the right collection for fixed ordered data or unique values.

## Key concepts
- A **tuple** is an ordered immutable collection: `server = ("api", 8)`. Index it with `server[0]`; its elements cannot be reassigned.
- A **set** holds unique hashable values: `zones = {"a", "b"}`. Add with `zones.add("c")`, remove safely with `zones.discard("a")`.
- Use `in` to test membership, `len()` to count items.
- Sets support `|` (union), `&` (intersection), and `-` (difference).
- Set iteration order is not guaranteed. Use `sorted(my_set)` when output order matters.
- An empty set is `set()`, not `{}` (an empty dictionary).

## Small example
```python
server = ("api", 8)
tags = {"blue", "green", "blue"}
print(server[0])
print(len(tags))
```

## Trade-offs
Use tuples when positions and immutability matter. Use sets for uniqueness and fast membership checks; use lists when element order or duplicates matter.

## Practice
Read [diy.md](diy.md). Run `bash diy.sh` to start local practice. Reference: [08_tuples_sets.py](08_tuples_sets.py).

Run the example from the repository root:
```bash
python lesson-8-sets/08_tuples_sets.py
```

Expected:
```text
Server: api
Unique zones: 2
Common zones: ['east']
All zones: ['east', 'north', 'south', 'west']
```

No external dependencies.

## Important line notes

- A tuple is immutable; sets remove duplicate zones; `&` finds common zones and `|` combines unique zones.
