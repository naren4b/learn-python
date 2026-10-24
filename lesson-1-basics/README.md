# Day 1: Python syntax and variables

## Objective
Write a short Python program using variables, comments, indentation, `if` and `print()`.

## Key points
- `#` starts a comment.
- `name = "Python"` assigns a value without an explicit type declaration.
- `True` and `False` start with capitals.
- A colon `:` begins a code block. Indent its body with four spaces.
- `print()` writes output. No semicolons or braces are needed.

## Practice
1. Follow [diy.md](diy.md) to create your own file **without copying** the reference solution.
2. Run it with the Python available in your WSL terminal. Python 3.12.x is suitable for this lesson.
3. Change `is_ready` from `True` to `False`. Predict which lines stop printing, then verify.
4. Ask questions before marking the lesson complete.

## Run in WSL
From the repository root:

```bash
python day-1/01_basics.py
```

## Run in isolated Podman
```bash
podman run --rm -v "$PWD:/work" -w /work \
  docker.io/library/python:3.12.14-slim-bookworm \
  python day-1/01_basics.py
```

The complete reference solution is [01_basics.py](01_basics.py). No packages are needed; `requirements.txt` is empty.

## Expected output
```text
Language: Python
Version: 3
Ready to learn!
Indentation defines this block
Program completed
```

## Trade-off
Python uses indentation to mark blocks. Consistent four-space indentation matters.

## Common syntax fixes

- Use a comma to separate text and variables: `print("My Age is", age)`.
- An `else` statement needs a colon: `else:`.
- Use consistent indentation inside `if` and `else` blocks.

The learner moved to the next lesson after practicing these fixes.

## Important line notes

- `if is_ready:` checks a boolean; the four-space indentation controls which lines belong to the block.
