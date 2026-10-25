# Lesson 17 — Iterators and Generators

## Concepts

An **iterable** produces an iterator through `iter()`. Calling `next()` gets the next item; when finished it raises `StopIteration`.

A **generator** function uses `yield` to produce one item at a time, resuming from where it paused. A `for` loop handles iteration automatically.

```python
def count_up_to(limit):
    for n in range(1, limit + 1):
        yield n

for value in count_up_to(3):
    print(value)
```

## Useful operations

| Operation | Purpose |
| --- | --- |
| `iter(items)` | Obtain iterator from iterable |
| `next(iterator)` | Get next item |
| `yield item` | Produce item lazily from generator |
| `enumerate(items, start=1)` | Index items |
| `zip(names, ports)` | Pair corresponding items |

## Key points

- Lists store their elements; generators can compute values one by one.
- Iterators can be exhausted; requesting the next element after exhaustion raises `StopIteration`.
- Generator functions do not execute until iterated.
- Laziness is useful for streams and large data, but is not always faster.

See [DIY](diy.md) and [reference](17_iterators.py).

Official docs: [Iterators](https://docs.python.org/3.12/tutorial/classes.html#iterators) · [Generators](https://docs.python.org/3.12/tutorial/classes.html#generators).
