# Learn Python

Learn Python by writing and running small programs. Start with Day 0 and follow the lessons in order. This repository is generic and open to anyone.

## Setup (Windows + WSL + Podman)

Requirements: WSL, Podman, and a text editor such as Notepad. Python is provided by the container, so you do not need to install it on Windows.

Open WSL and use your existing checkout:

```bash
cd /mnt/c/code/personal/learn-python
git pull --ff-only origin main
podman run --rm docker.io/library/python:3.12.14-slim-bookworm python --version
```

Expected: `Python 3.12.14`.

Run a lesson from the repository root:

```bash
podman run --rm -v "$PWD:/work" -w /work \
  docker.io/library/python:3.12.14-slim-bookworm \
  python day-0/00_hello.py
```

Expected: `Hello, Python!`

If you use a different local checkout location, change only the `cd` command. No extra working directory is needed.

## How to learn

1. Open the current day's `README.md` and read the objective and key points.
2. Open its `.py` file in Notepad. Run it using Podman.
3. Change the program as suggested in the exercise. Save and run again.
4. Explain what changed and check the output before moving to the next day.

Each day contains one short `README.md`, one runnable Python file, and `requirements.txt` (with no dependencies when none are needed). Extra packages, where required, will be explained in that day's README.

## Learning path

| Day | Topic | Status |
| --- | --- | --- |
| [Day 0](day-0/README.md) | Setup, save and run Python | Ready to test |
| Day 1 | Syntax, indentation, comments and variables | Planned |
| Day 2 | Strings, integers, floats and booleans | Planned |
| Day 3+ | Operators, functions, classes, control flow, collections, files, APIs and tests | Planned |
| Later | Easy and medium coding exercises | Planned |

Practice one topic at a time. New lessons arrive through reviewed pull requests and are collected on `main`.

## Archived examples

Old examples are retained unchanged under [archive](archive/learn-rest/get_json_data.py). They are historical material, not part of the ordered beginner-to-interview learning path. The archived REST example uses the external `requests` package and requires network access.

## Contribution rules

Keep examples small, runnable and company-independent. Never commit credentials. Prefer Python's standard library unless an external package is essential. Add diagrams only where they make the explanation easier to understand.
