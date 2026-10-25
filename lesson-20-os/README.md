# Lesson 20 — OS environment and subprocess

## Goal

Use Python's `os`, `pathlib` and `subprocess` modules safely in automation scripts.

| Tool | Purpose | Example |
| --- | --- | --- |
| `os.getenv()` | Read optional environment setting | `os.getenv("APP_ENV", "dev")` |
| `os.environ["KEY"]` | Read required environment setting | Raises `KeyError` if missing |
| `Path.cwd()` | Current working directory | `Path.cwd()` |
| `subprocess.run()` | Execute external commands | `subprocess.run(["python", "--version"])` |
| `os.environ.copy()` | Prepare child process environment | Copy then override variables |

## Execute commands safely

```python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "--version"],
    capture_output=True,
    text=True,
    check=True,
    timeout=10,
)
print(result.stdout or result.stderr)
```

## Important lines

- Pass a **list of arguments** to `subprocess.run()`, rather than building a shell command string.
- `sys.executable` selects the current Python interpreter.
- `capture_output=True` captures output instead of printing directly.
- `text=True` decodes captured bytes into strings.
- `check=True` raises `CalledProcessError` for non-zero exit codes.
- `timeout=10` raises `TimeoutExpired` if the command takes too long.
- Avoid `shell=True` with untrusted input; shell expansion and injection can occur.
- Environment variable values are strings and inherited by child processes unless overridden.

## Environment for a child process

```python
import os
import subprocess
import sys

env = os.environ.copy()
env["APP_ENV"] = "test"
subprocess.run(
    [sys.executable, "-c", "import os; print(os.getenv('APP_ENV'))"],
    env=env,
    check=True,
)
```

This changes the environment **only for the child process**, not the parent shell.

[DIY](diy.md) · [Reference](20_os_subprocess.py)

Official documentation: [os](https://docs.python.org/3.12/library/os.html) · [subprocess](https://docs.python.org/3.12/library/subprocess.html) · [pathlib](https://docs.python.org/3.12/library/pathlib.html)
