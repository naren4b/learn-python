# Day 5: For and while loops

## Objective
Repeat work with `for` and `while` loops.

## Concepts
- A `for` loop processes each value from an iterable. `range(start, stop)` excludes `stop`.
- A `while` loop runs while its condition is true.
- `break` exits a loop; `continue` skips to the next iteration.

## Syntax
```python
for n in range(1, 4):
    print(n)

count = 1
while count <= 3:
    print(count)
    count += 1
```

## Important points
- Indent loop bodies by four spaces.
- Update the condition variable in a `while` loop to avoid an unintended infinite loop.
- Prefer `for` for a known sequence; use `while` when repetition depends on a changing condition.

## Practice
Read [diy.md](diy.md), then implement it in your ignored `lab/app.py`. Root [diy.sh](../diy.sh) clears the scratch files and opens `vi`. The [reference example](05_loops.py) is available if needed.

## Run reference from repository root
```bash
python day-5/05_loops.py
```

Expected:
```text
Total: 15
Countdown: 3
Countdown: 2
Countdown: 1
Done
```

Standard library only; no external dependencies.

## Important line notes

- `range(1, 6)` generates 1 through 5; `count -= 1` prevents an endless countdown.
