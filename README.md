# Learn Python

Learn Python by writing and running small programs. Start with Day 0 and follow the lessons in order. This repository is generic and open to anyone.

## Setup (Windows + WSL + Podman)

Requirements: WSL and Python 3.12 for hands-on practice, plus a text editor such as `vi`. Podman is optional for isolated runs with the pinned Python 3.12.14 image.

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

1. Open the current day's `README.md` to understand the objective and key points.
2. Follow `diy.md`. From the repository root, run `bash diy.sh` to reset and open the ignored `lab/app.py` in `vi`. After exiting, run `python lab/app.py` in WSL. Do not commit the local exercise. Create `lab/` with `mkdir -p lab` before entering it. Use the lesson's reference `.py` only if needed.
3. Change the program as suggested in the exercise. Save and run again. Ask questions and mark the lesson finished before the next PR is merged.
4. Explain what changed and check the output before moving to the next day.

Each day contains one short `README.md`, a `diy.md` with the fixed local `app.py` workflow, one runnable reference Python file, and `requirements.txt` (with no dependencies when none are needed). Extra packages, where required, will be explained in that day's README.

## Complete refresher roadmap

See [Python refresher roadmap](curriculum/README.md) for the core Python, practical automation, interview problem tracks and the standard lesson folder skeleton. Planned topics are outlines only; working reference code is created when that lesson starts.

## Learning path

| Day | Topic | Status |
| --- | --- | --- |
| [Day 0](day-0/README.md) | Setup, save and run Python | Completed |
| [Day 1](day-1/README.md) | Syntax, indentation, comments and variables | Completed |
| [Day 2](day-2/README.md) | Strings, integers, floats and booleans | Completed |
| [Day 3](day-3/README.md) | Arithmetic, comparison and logical operators | Completed |
| [Day 4](day-4/README.md) | Functions and return values | Completed (advanced by learner) |
| [Day 5](day-5/README.md) | For and while loops | Advanced by learner |
| [Day 6](day-6/README.md) | Lists and iteration | Completed (advanced by learner) |
| [Day 7](day-7/README.md) | Dictionaries and key-value data | In progress (PR open) |
| Day 8+ | Tuples/sets, strings, collections, exceptions, files, APIs, testing and coding exercises | [Planned topics](curriculum/README.md) |
| Later | Easy and medium coding exercises | Planned |

Practice one topic at a time. The maintainer prepares reference code and documentation on a task branch. Learners do not need to commit their practice code. Lessons are merged to `main` once completed and reviewed.

## Archived examples

Older lessons and experiments are preserved under [archive/legacy-days](archive/legacy-days/01/README.md), [archive/setup.md](archive/setup.md) and [archive/learn-rest](archive/learn-rest/get_json_data.py). They are historical material, not part of the ordered learning path. Some examples use external packages, network access or an older runtime.

## Contribution rules

Keep examples small, runnable and company-independent. Never commit credentials. Prefer Python's standard library unless an external package is essential. Add diagrams only where they make the explanation easier to understand.
