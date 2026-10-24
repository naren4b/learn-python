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
Run `python lesson-10-comp/10_comprehensions.py` from the repository root.

Expected output:
```text
Sorted: [5, 5, 10, 20, 30]
Doubled: [10, 10, 20, 40, 60]
Above 10: [20, 30]
Name lengths: {'api': 3, 'worker': 6}
Unique: [5, 10, 20, 30]
```

Read [diy.md](diy.md) and use root [diy.sh](../diy.sh). No external dependencies.

## Questions from practice

- List comprehension syntax is `[expression for item in values if condition]`. The expression transforms the selected values; the optional condition filters them.
- Use `==` to compare values, not `=`.
- Dictionary comprehension uses `{key_expression: value_expression for item in values}`, e.g. `{name: len(name) for name in names}`.
- `[]` creates a list comprehension, `{}` with one expression creates a set comprehension, `{key: value ...}` creates a dictionary comprehension, and `()` creates a generator expression.
- In a function signature, `-> int` indicates the intended return type; annotations are not automatically enforced by Python.
- Other symbols to recognize: `:=` assignment expression, `@` decorator, `*args` positional arguments, and `**kwargs` keyword arguments. Their deeper use belongs in later function/OOP lessons.

## Important line notes

- `sorted()` returns a new list; comprehensions transform or filter values; set comprehensions remove duplicates.
