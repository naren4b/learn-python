# Python refresher roadmap

This is the **curriculum skeleton**, not a claim that future lessons are implemented. Complete each lesson's four files only when that day becomes active. Topics are adaptable; experienced learners can skip exercise steps, but the maintainer still supplies complete GitHub learning material.

## Track A: Core Python

| Day | Topic | Refresh checklist | Status |
| --- | --- | --- | --- |
| 0 | Environment | WSL, run Python, optional Podman | Completed |
| 1 | Syntax and variables | indentation, comments, assignment, print | Completed |
| 2 | Data types | str, int, float, bool, conversion, f-strings | Completed |
| 3 | Operators and branching | arithmetic, remainder, comparison, and/or/not, if/else | Completed |
| 4 | Functions | def, parameters, return, scope basics | Completed |
| 5 | Loops | range, for, while, break, continue | Completed |
| 6 | Lists | indexing, append, iteration, len, sum | Completed |
| 7 | Dictionaries | key/value access, get, update, items | Completed |
| 8 | Tuples and sets | immutability, uniqueness, membership, set operations | Reference merged |
| 9 | Strings | slicing, split/join, strip, replace, find, formatting | Completed |
| 10 | Collections and comprehensions | slicing, sorting, list/dict/set comprehensions | Completed |
| 11 | Functions and arguments | def, return vs print, defaults, *args/**kwargs, lambda, local/global scope | Reference merged |
| 12 | Exceptions | try/except/else/finally, raising errors | Reference merged |
| 13 | File handling basics | with/open, read/write/append, encodings, pathlib, text files | Practice complete; PR #19 open |
| 14 | CSV, JSON and YAML files | csv.reader/DictReader/DictWriter, json.load/dump, YAML safe_load/safe_dump with PyYAML, parsing and validation | Completed |
| 15 | Modules and packages | import, __name__, pip/venv, requirements | Completed |
| 16 | Classes and OOP basics | class, object, __init__, self, instance attributes, methods, encapsulation, inheritance, dataclasses | Completed |
| 17 | Iterators and generators | iterable, yield, enumerate, zip | Completed |
| 18 | Useful standard library | collections, itertools, datetime, re | Completed |

## Specific refresh coverage

- **Functions:** define/call functions, positional and keyword arguments, defaults, return values, scope, and basic type annotations.
- **Classes/OOP:** instantiate objects, constructors (`__init__`), `self`, instance vs class attributes, instance methods, simple inheritance and composition.
- **File handling:** use `with open(...)` and `pathlib.Path` for text files; read/write CSV with `csv`, JSON with `json`, and YAML with `PyYAML` (`yaml.safe_load` / `yaml.safe_dump`). Unlike CSV and JSON, YAML requires an external dependency recorded in `requirements.txt`.
- Include small standalone exercises for **reading, modifying and writing each format**, including errors for missing or malformed files. Keep sample files generic and free of secrets.

## Track B: Practical Python

| Day | Topic | Refresh checklist |
| --- | --- | --- |
| 19 | CLI scripts | argparse, input, exit codes, logging |
| 20 | OS and subprocess | os, environment variables, subprocess, safety |
| 20A | NumPy foundations (supplement) | ndarray, shapes, slicing, vectorized operations, basic statistics; install with uv |
| 20B | Pandas foundations (supplement) | DataFrames, CSV/JSON, filtering, groupby, join/merge; install with uv |
| 21 | HTTP and APIs | requests or urllib, timeouts, status codes, parsing |
| 22 | Unit tests | unittest/pytest, assertions, fixtures, mocks |
| 23 | Type hints and clean code | annotations, linting, readability, error handling |
| 24 | Concurrency basics | threads, asyncio, when not to use them |
| 25 | Mini project | input → processing → output, validation, tests |

## Track C: Coding interview drills

Progress by skill, not rigid day count:

1. Arrays/lists: counting, min/max, two pointers.
2. Strings: palindrome, frequency, substring basics.
3. Dictionaries/sets: lookups, duplicates, counting.
4. Sorting and searching: built-ins, binary search.
5. Stacks and queues: validation, traversal.
6. Problem-solving: clarify constraints, edge cases, time/space complexity, 25-minute timed rounds.

## Lesson skeleton

```text
learn-python/
├── README.md                    # public entrypoint and progress
├── ai-instructions.md           # maintainer and teaching rules
├── diy.sh                       # reset ignored lab/ and open editor
├── curriculum/
│   └── README.md                # all future topics (this file)
├── lesson-N-abbr/
│   ├── README.md                # objective, concise explanation, examples, output
│   ├── diy.md                   # pseudocode and Your Exercise
│   ├── NN_topic.py              # fully runnable reference implementation
│   └── requirements.txt         # empty unless dependencies needed
├── lab/                         # ignored learner scratch files, never commit
└── archive/                     # historical examples
```

## Publishing and progress rules

- Only create a new `day-N/` directory when preparing that day's lesson, so planned days cannot be mistaken for finished reference implementations.
- The maintainer creates a new branch and PR, fills all four lesson files, and updates the learning index.
- Keep the current PR open until the learner says `next` or `lesson completed`.
- Record learner questions that add useful knowledge. Full exercise completion is optional when competence is demonstrated.
- In chat provide links and a short **Your Exercise** section; omit full `diy.md` and pseudocode.
