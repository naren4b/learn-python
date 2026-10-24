# Day 10: Collections, sorting and comprehensions

## Objective
Transform and filter collections with readable comprehensions.

## Concepts
- `sorted(values)` returns a new sorted list; `values.sort()` modifies an existing list.
- List comprehension: `[x * 2 for x in values]`.
- Add an optional filter: `[x for x in values if x > 10]`.
- Dictionary comprehension: `{name: len(name) for name in names}`.
- Set comprehension: `{x for x in values}` removes duplicates.
- Slices use `values[start:stop:step]`; `stop` is excluded.

## Trade-offs
Comprehensions are concise for simple transformations. Prefer ordinary loops when logic becomes difficult to follow. Sorting creates a new list with `sorted()`, while `.sort()` mutates the list.

## Reference
Run `python day-10/10_comprehensions.py` from the repository root.

Expected output:
```text
Sorted: [5, 5, 10, 20, 30]
Doubled: [10, 10, 20, 40, 60]
Above 10: [20, 30]
Name lengths: {'api': 3, 'worker': 6}
Unique: [5, 10, 20, 30]
```

Read [diy.md](diy.md) and use root [diy.sh](../diy.sh). No external dependencies.
