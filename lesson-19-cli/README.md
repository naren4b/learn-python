# Lesson 19 — Command-line input and argparse

## Goal
Read user input, positional arguments, and named command-line options.

| Tool | Use | Example |
| --- | --- | --- |
| `input()` | Ask interactively at runtime | `name = input('Name: ')` |
| `sys.argv` | Access raw command-line arguments | `sys.argv[1:]` |
| `argparse.ArgumentParser` | Parse validated positional and optional arguments | `parser.add_argument('--port', type=int)` |

## Example

```python
import argparse

parser = argparse.ArgumentParser(description='Describe a service')
parser.add_argument('name', help='Service name')
parser.add_argument('--port', type=int, default=8080)
args = parser.parse_args()
print(f'{args.name}:{args.port}')
```

Run: `python app.py api --port 9090`

Output: `api:9090`

## Read environment variables

Use `os.getenv()` for an optional variable or `os.environ["NAME"]` when a missing variable should raise `KeyError`.

```python
import os

port = int(os.getenv("APP_PORT", "8080"))  # Default if unset
token = os.environ.get("API_TOKEN")        # None if unset
print(port)
```

In WSL, set and pass a variable to the Python process:

```bash
export APP_PORT=9090
python lab/app.py
# Or only for one command:
APP_PORT=9090 python lab/app.py
```

- All environment variable values are strings; convert when needed.
- `os.getenv("APP_PORT", "8080")` returns the default only when the variable is **unset**, not when it is an empty string.
- Never print or commit credentials such as `API_TOKEN`.

See [official `os.environ` documentation](https://docs.python.org/3.12/library/os.html#os.environ). Lesson 20 explores environment variables and subprocesses in depth.

## Important notes

- `argparse` generates `--help` text automatically.
- `type=int` converts and validates the CLI argument.
- `default=8080` is used when the user does not pass `--port`.
- Command-line argument strings are separate from interactive `input()`.
- Guard runnable code with `if __name__ == '__main__':` so importing does not parse CLI arguments.

[DIY](diy.md) · [Reference](19_cli.py) · [Official argparse documentation](https://docs.python.org/3.12/library/argparse.html) · [sys.argv](https://docs.python.org/3.12/library/sys.html#sys.argv)
