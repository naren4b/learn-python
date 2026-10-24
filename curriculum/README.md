# Python refresher roadmap

This is the **curriculum skeleton**, not a claim that future lessons are implemented. Complete each lesson's four files only when that day becomes active. Topics are adaptable; experienced learners can skip exercise steps, but the maintainer still supplies complete GitHub learning material.

## Track A: Core Python

| Day | Topic | Refresh checklist | Status |
| --- | --- | --- | --- |
| 0 | Environment | WSL, run Python, optional Podman | Completed |
| 1 | Syntax and variables | indentation, comments, assignment, print | Completed |
| 2 | Data types | str, int, float, bool, conversion, f-strings | Completed |
| 3 | Operators and branching | arithmetic, remainder, comparison, and/or/not, if/else | Completed |
| 4 | Functions | def, parameters, return, scope basics | Advanced |
| 5 | Loops | range, for, while, break, continue | Advanced |
| 6 | Lists | indexing, append, iteration, len, sum | Completed |
| 7 | Dictionaries | key/value access, get, update, items | Active: PR #11 |
| 8 | Tuples and sets | immutability, uniqueness, membership, set operations | Planned |
| 9 | Strings | slicing, split/join, strip, replace, find, formatting | Planned |
| 10 | Collections and comprehensions | slicing, sorting, list/dict/set comprehensions | Planned |
| 11 | Functions deeper | defaults, *args/**kwargs, lambda, scope | Planned |
| 12 | Exceptions | try/except/else/finally, raising errors | Planned |
| 13 | Files and paths | with/open, pathlib, text files | Planned |
| 14 | JSON and CSV | load/dump, reading/writing structured data | Planned |
| 15 | Modules and packages | import, __name__, pip/venv, requirements | Planned |
| 16 | Object-oriented Python | classes, __init__, methods, dataclasses | Planned |
| 17 | Iterators and generators | iterable, yield, enumerate, zip | Planned |
| 18 | Useful standard library | collections, itertools, datetime, re | Planned |

## Track B: Practical Python

| Day | Topic | Refresh checklist |
| --- | --- | --- |
| 19 | CLI scripts | argparse, input, exit codes, logging |
| 20 | OS and subprocess | os, environment variables, subprocess, safety |
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
├── day-N/
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
