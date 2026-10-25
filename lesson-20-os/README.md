# Lesson 20 — Execute Bash scripts and collect structured results

## Goal

Execute a Bash script from Python and turn its output into a Python dictionary.

We covered reading environment variables in [Lesson 19](../lesson-19-cli/README.md). Here we focus on using `subprocess` to connect Bash and Python.

## Approach: Bash emits JSON, Python loads a dictionary

**Bash (`status.sh`)**

```bash
#!/usr/bin/env bash
set -euo pipefail
printf '{"service":"api","status":"healthy","port":8080}\n'
```

**Python**

```python
import json
import subprocess

result = subprocess.run(
    ["bash", "status.sh"],
    capture_output=True,
    text=True,
    check=True,
    timeout=10,
)
status = json.loads(result.stdout)  # JSON object -> Python dict
print(status["service"], status["status"])
```

## Key points

- `subprocess.run(["bash", "status.sh"])` runs the script and waits for completion.
- `capture_output=True` collects stdout and stderr separately.
- `text=True` returns strings, not bytes.
- `check=True` raises `CalledProcessError` on nonzero exit.
- `json.loads(result.stdout)` parses valid JSON into a dict (when Bash emits a JSON object).
- Keep stdout **JSON-only**. Send diagnostics to stderr: `echo "debug" >&2`.
- Use `json.loads` instead of manually splitting output. Invalid JSON raises `JSONDecodeError`.
- Use argument lists, not `shell=True`, and set a timeout for external processes.
- For real scripts, construct JSON safely (e.g. with `jq -n --arg`) rather than interpolating untrusted values inside JSON.

Run the reference from this folder:

```bash
cd lesson-20-os
python 20_os_subprocess.py
```

[DIY](diy.md) · [Python reference](20_os_subprocess.py) · [Bash reference](status.sh) · [Python subprocess docs](https://docs.python.org/3.12/library/subprocess.html) · [JSON docs](https://docs.python.org/3.12/library/json.html)
