# Learn Python

Hands-on Python learning, one small runnable lesson at a time. Examples are useful for anyone refreshing Python or preparing for coding interviews.

## Lessons

| Day | Topic | Status |
| --- | --- | --- |
| [Day 0](day-0/README.md) | Run Python 3.12.14 with Podman | Ready to test |
| Day 1 | Syntax, variables and comments | Planned |
| Day 2 | Strings, numbers and booleans | Planned |
| Day 3+ | Operators, functions, control flow, collections, files, APIs, tests and coding practice | Planned |

## Layout

Each completed day is a directory: `day-0/`, `day-1/`, and so on. Each contains:
- One-page `README.md` with objective, key ideas, commands, practice and trade-offs.
- A complete runnable `.py` example.
- `requirements.txt`, empty of dependencies when none are needed.

Existing examples, including [REST examples](learn-rest/get_json_data.py), are preserved until they can be reviewed and reorganized.

## Learning workflow

1. Practice locally with Notepad, WSL and Podman.
2. Keep one day per directory and one focused change per pull request.
3. Review and merge verified lessons into `main`. Avoid direct commits to `main`.
4. Keep examples generic. No company interview content, credentials, cloud accounts or required IDE.

Run Day 0 before moving to Day 1. The official Python image is pinned at `docker.io/library/python:3.12.14-slim-bookworm`.
