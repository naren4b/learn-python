# Day 1: Do it yourself

Use WSL. Type the code yourself, without opening the reference implementation.

```bash
cd /mnt/c/code/personal/learn-python
mkdir -p day-1
touch day-1/01_basics.py
vi day-1/01_basics.py
```

Write a program that:
1. Stores the language name in `name` as a string.
2. Stores version number `3` in `version`.
3. Stores `True` in `is_ready`.
4. Prints the language and version.
5. Uses `if is_ready:` to print **two indented messages**.
6. Prints `Program completed` outside the block.

Save and run:

```bash
python day-1/01_basics.py
```

Now change `is_ready` to `False`. Run again and explain why the output changed. Use [the reference code](01_basics.py) only if stuck.

No `pip install` is required for this lesson.
