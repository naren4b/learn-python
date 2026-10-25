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
  python lesson-0-hello/00_hello.py
```

Expected: `Hello, Python!`

If you use a different local checkout location, change only the `cd` command. No extra working directory is needed.

## How to learn

1. Open the current day's `README.md` to understand the objective and key points.
2. Follow `diy.md`. From the repository root, run `bash diy.sh` to reset and open the ignored `lab/app.py` in `vi`. After exiting, run `python lab/app.py` in WSL. Do not commit the local exercise. Create `lab/` with `mkdir -p lab` before entering it. Use the lesson's reference `.py` only if needed.
3. Change the program as suggested in the exercise. Save and run again. Ask questions and mark the lesson finished before the next PR is merged.
4. Explain what changed and check the output before moving to the next day.

Each lesson contains one short `README.md`, a `diy.md` with the fixed local `app.py` workflow, one runnable reference Python file, and `requirements.txt` (with no dependencies when none are needed). Extra packages, where required, will be explained in that day's README.

## Complete refresher roadmap

See [Python refresher roadmap](curriculum/README.md) for the core Python, practical automation, interview problem tracks and the standard lesson folder skeleton. Planned topics are outlines only; working reference code is created when that lesson starts.

## Learning path

| Day | Topic | Status |
| --- | --- | --- |
| [Day 0](lesson-0-hello/README.md) | Setup, save and run Python | Completed |
| [Day 1](lesson-1-basics/README.md) | Syntax, indentation, comments and variables | Completed |
| [Day 2](lesson-2-types/README.md) | Strings, integers, floats and booleans | Completed |
| [Day 3](lesson-3-ops/README.md) | Arithmetic, comparison and logical operators | Completed |
| [Day 4](lesson-4-func/README.md) | Functions and return values | Completed |
| [Day 5](lesson-5-loops/README.md) | For and while loops | Completed |
| [Day 6](lesson-6-lists/README.md) | Lists and iteration | Completed |
| [Day 7](lesson-7-dict/README.md) | Dictionaries and key-value data | Completed |
| [Day 8](lesson-8-sets/README.md) | Tuples and sets | Reference merged; practice not submitted |
| [Day 9](lesson-9-strings/README.md) | Strings and text processing | Completed |
| [Day 10](lesson-10-comp/README.md) | Collections, sorting and comprehensions | Completed |
| [Lesson 11](lesson-11-func-args/README.md) | Functions and arguments | Reference merged; practice reviewed |
| [Lesson 12](lesson-12-except/README.md) | Exception handling | Reference merged |
| Lesson 13 | Text file handling | Practice complete; [PR #19](https://github.com/naren4b/learn-python/pull/19) pending merge |
| [Lesson 14](lesson-14-data/README.md) | CSV, JSON and YAML | Completed |
| [Lesson 15](lesson-15-modules/README.md) | Modules, packages and imports | Completed |
| [Lesson 16](lesson-16-oop/README.md) | Classes and OOP | Completed |
| [Lesson 17](lesson-17-iter-gen/README.md) | Iterators and generators | Completed |
| [Lesson 18](lesson-18-stdlib/README.md) | Standard library | Completed |
| [Lesson 19](lesson-19-cli/README.md) | sys, argparse and os inputs | Completed |
| [Lesson 20](lesson-20-os/README.md) | Bash/Docker subprocess and JSON | Completed |
| [Lesson 21](lesson-21-apis/README.md) | HTTP APIs and pagination | Completed |
| [Lesson 22](lesson-22-tests/README.md) | Unit testing | Practice skipped; PR #29 open |
| [Lesson 23](lesson-23-types/README.md) | Type hints | Skipped; PR #30 open |
| Lesson 24 | Concurrency | Skipped |
| [Lesson 25](lesson-25-boto3/README.md) | AWS automation with Boto3 | Current lesson (PR open) |
| Lesson 26 | Kubernetes Python client | Next |
| Later | NumPy, Pandas and coding exercises | Planned |
| Later | Easy and medium coding exercises | Planned |

Practice one topic at a time. The maintainer prepares reference code and documentation on a task branch. Learners do not need to commit their practice code. Lessons are merged to `main` once completed and reviewed.

## Archived examples

Older lessons and experiments are preserved under [archive/legacy-days](archive/legacy-days/01/README.md), [archive/setup.md](archive/setup.md) and [archive/learn-rest](archive/learn-rest/get_json_data.py). They are historical material, not part of the ordered learning path. Some examples use external packages, network access or an older runtime.

## Contribution rules

Keep examples small, runnable and company-independent. Never commit credentials. Prefer Python's standard library unless an external package is essential. Add diagrams only where they make the explanation easier to understand.
