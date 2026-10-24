# Day 1: Do it yourself

In WSL, use your local scratch file. Type the solution yourself.

```bash
mkdir -p /mnt/c/code/personal/learn-python/lab
cd /mnt/c/code/personal/learn-python/lab
touch app.py requirements.txt
vi app.py
python app.py
```

In `app.py`:
1. Set `name` to the string `"Python"`.
2. Set `version` to the integer `3`.
3. Set `is_ready` to `True`.
4. Print the language and version.
5. Use `if is_ready:` to print two messages, indented four spaces.
6. Print `Program completed` outside the `if` block.

Change `is_ready` to `False`, save and run `python app.py` again. Explain what changes.

No packages to install. Do not commit your local `app.py`. Use [the reference code](01_basics.py) only if stuck.
