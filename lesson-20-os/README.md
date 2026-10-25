# Lesson 20 — Subprocess and external commands

## Goal
Execute external commands from Python using the standard-library `subprocess` module.

Environment variables (`os.getenv()` and `os.environ`) were covered in [Lesson 19](../lesson-19-cli/README.md). This lesson does not repeat them.

## Core operations

| Operation | Purpose |
| --- | --- |
| `subprocess.run(["command", "arg"])` | Run a command and wait |
| `capture_output=True` | Capture stdout and stderr |
| `text=True` | Receive output as strings |
| `check=True` | Raise `CalledProcessError` on failure |
| `timeout=10` | Limit how long a command may run |
| `result.returncode` | Inspect exit status |
| `result.stdout` / `result.stderr` | Read captured output |

## Example

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

print((result.stdout or result.stderr).strip())
print("Exit code:", result.returncode)
```

- `sys.executable` points to the Python interpreter executing this program.
- Prefer an **argument list** rather than a constructed shell-command string.
- Avoid `shell=True` with untrusted values to prevent shell injection.
- Use `try/except subprocess.CalledProcessError` and `subprocess.TimeoutExpired` where failures need handling.

Run: `python lesson-20-os/20_os_subprocess.py`.

[DIY](diy.md) · [Reference](20_os_subprocess.py) · [Official subprocess docs](https://docs.python.org/3.12/library/subprocess.html)
