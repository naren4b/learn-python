# Day 6: Python lists

## Objective
Store and process ordered values with lists.

## Concepts
- A list is ordered and mutable: `numbers = [10, 20]`.
- Indexes begin at 0; `numbers[-1]` is the last element.
- `append(value)` adds one item to the end.
- `len(numbers)` counts elements.
- Iterate with `for number in numbers:`.
- `sum(numbers)` adds numeric values.

## Syntax
```python
numbers = [10, 20, 30]
numbers.append(40)
print(numbers[0], numbers[-1])
print(len(numbers), sum(numbers))
```

## Trade-offs
Lists keep insertion order and allow changes; finding a value typically scans items. Indexing outside the list raises `IndexError`.

## Practice and run
See [diy.md](diy.md). From the repository root use `bash diy.sh` to start local practice; reference: [06_lists.py](06_lists.py).

```bash
python lesson-6-lists/06_lists.py
```

Expected:
```text
First: 120
Last: 160
Count: 4
Total: 550
Average: 137.50
```

No dependencies.

## Learning notes
The learner used a `for` loop to accumulate the total of `[143, 26, 32, 43, 200]` (= `444`), printed the values, appended `33`, and counted 6 items. That correctly demonstrates iteration, list mutation, and length. The full exercise is optional when the learner demonstrates confidence; the repository reference and learning notes must still be complete.

## Important line notes

- `append()` modifies a list, `[-1]` retrieves its last element, and `sum()/len()` computes the average.
