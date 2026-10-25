# Lesson 19 — Python process inputs: sys, argparse and os

## Goal

Learn **two ways to read command-line arguments** and **one way to read environment variables**. These are Python **standard-library modules** (not external packages).

| Module | How to read | Purpose |
| --- | --- | --- |
| `sys` | `sys.argv` | Raw CLI arguments, like Bash `$0`, `$1`, `"$@"` |
| `argparse` | `ArgumentParser().parse_args()` | Declarative CLI parsing, named options, types, defaults and `--help` |
| `os` | `os.getenv()` / `os.environ` | Environment variables inherited by the Python process |

## 1. sys — read raw CLI arguments

```python
import sys

print(sys.argv[0])   # Script path, similar to Bash $0
print(sys.argv[1:])  # Arguments supplied by the caller
```

Running `python app.py api --port 9090` produces `['api', '--port', '9090']` for `sys.argv[1:]`. Everything is a string, including `--port`; Python does **not** interpret it for you.

| Bash | Python |
| --- | --- |
| `$0` | `sys.argv[0]` |
| `$1` | `sys.argv[1]` |
| `$#` | `len(sys.argv) - 1` |
| `"$@"` | `sys.argv[1:]` |

## 2. argparse — declarative CLI arguments

```python
import argparse

parser = argparse.ArgumentParser(description="Describe a service")
parser.add_argument("service")                     # Required positional
parser.add_argument("--port", type=int, default=8080)  # Optional named
args = parser.parse_args()
print(f"{args.service}:{args.port}")
```

Run `python app.py api --port 9090` → `api:9090`.

- Positional arguments are assigned in declared order.
- Named options such as `--port` can usually appear before or after positional arguments.
- `type=int` validates/converts; `default=8080` applies when the option is absent.
- `argparse` generates `--help` and reports unexpected arguments.

## 3. os — read environment variables

```python
import os

port = int(os.getenv("APP_PORT", "8080"))  # Default when unset
token = os.environ.get("API_TOKEN")        # None when unset
# os.environ["API_TOKEN"] raises KeyError if missing.
```

In WSL:

```bash
export APP_PORT=9090
python app.py

# Alternatively, set the variable only for this command
APP_PORT=9090 python app.py
```

All environment variable values are strings. The `os.getenv` default applies when the variable is **unset**, not when its value is an empty string. Never print or commit credentials.

## What to choose

- Choose **`sys.argv`** when you want raw argument strings and will implement parsing yourself.
- Choose **`argparse`** for most CLI tools: named flags, validation, usage information.
- Choose **`os.getenv` / `os.environ`** for environment-based configuration. These can be used together with either CLI approach.

[DIY](diy.md) · [Reference](19_cli.py)

Official docs: [sys.argv](https://docs.python.org/3.12/library/sys.html#sys.argv) · [argparse](https://docs.python.org/3.12/library/argparse.html) · [os.environ](https://docs.python.org/3.12/library/os.html#os.environ).
