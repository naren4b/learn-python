# Learn Python

Learn Python by writing and running small programs. Start with Day 0 and follow the lessons in order. This repository is generic and open to anyone.

## Python setups: choose the simplest that fits

| Setup | When to use | Trade-off |
| --- | --- | --- |
| Installed Python + standard library | **Start here for learning**; run `python lab/app.py` | No dependency isolation; avoid modifying OS-managed packages |
| `venv` + `pip` | Lightweight project isolation without extra tooling | Each project manages its own environment |
| `uv` + project virtual environment | **Recommended for everyday development** with external dependencies | Small upfront workflow change; maintains a shared package cache |
| Podman container | Reproducible, isolated runtime when needed | Container image and runtime overhead |

**Learning setup (recommended first):** Use an already installed Python 3.12 and an editor. From the repository root run `bash diy.sh`, then `python lab/app.py`. Standard-library modules such as `pathlib` and `tempfile` need no installation. Do not upgrade or install packages into an OS-managed Python just for these lessons.

**Everyday project setup (recommended):** Use `uv` with a project-specific `.venv` and declared dependencies. For a new project, `uv init`, `uv add requests`, and `uv run python main.py` provide a straightforward managed workflow. `uv` uses a shared package cache, reducing repeated downloads and potentially saving storage via links when the cache and environment are on compatible filesystems.

**Alternative:** Use `python -m venv .venv`, activate it, then `python -m pip install -r requirements.txt`. For containers, a Python 3.12 image under Podman is optional.

**Where imports come from:** Python searches locations in `sys.path`, including the script directory, standard library and environment-specific `site-packages` (or Debian/Ubuntu `dist-packages`). `python -m pip show <package>` reports an installed package's location; `import package; print(package.__file__)` shows its module file. `sys.prefix == sys.base_prefix` generally indicates the interpreter is not in a `venv`. Use `python -m pip` rather than an ambiguous standalone `pip` command when working with pip.

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
| [Lesson 13](lesson-13-files/README.md) | Text file handling | Current lesson (PR open) |
| Lesson 14+ | CSV, JSON, YAML, APIs and tests | [Planned topics](curriculum/README.md) |
| Later | Easy and medium coding exercises | Planned |

Practice one topic at a time. The maintainer prepares reference code and documentation on a task branch. Learners do not need to commit their practice code. Lessons are merged to `main` once completed and reviewed.

## Archived examples

Older lessons and experiments are preserved under [archive/legacy-days](archive/legacy-days/01/README.md), [archive/setup.md](archive/setup.md) and [archive/learn-rest](archive/learn-rest/get_json_data.py). They are historical material, not part of the ordered learning path. Some examples use external packages, network access or an older runtime.

## Contribution rules

Keep examples small, runnable and company-independent. Never commit credentials. Prefer Python's standard library unless an external package is essential. Add diagrams only where they make the explanation easier to understand.
