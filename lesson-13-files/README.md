# Lesson 13: Text file handling

## Goal
Safely read, write and append text using `pathlib.Path` and `with open()`.

## Main concepts
- `Path("notes.txt")` describes a filesystem path.
- `with path.open("w", encoding="utf-8") as file:` opens for writing, overwrites existing content, and closes automatically.
- `"a"` appends; `"r"` reads. `"x"` creates a new file but fails if it exists.
- `file.write(text)` writes text; `file.read()` retrieves it.
- `path.read_text(encoding="utf-8")` and `path.write_text(...)` are concise helpers.
- Handle `FileNotFoundError`, `PermissionError`, and decoding errors appropriately.

## Standard library modules used

| Module | Purpose | Used in this lesson |
| --- | --- | --- |
| `pathlib` | Object-oriented file and directory paths, including joining paths and reading/writing files | `Path(folder) / "services.txt"`, `path.open()`, `path.read_text()` |
| `tempfile` | Creates temporary files/directories safely for tests and experiments | `TemporaryDirectory()` creates a workspace that is cleaned up when its context exits |

Both are included with Python 3.12 and require **no pip installation**. `pathlib` makes file paths easier to handle across operating systems; `tempfile` helps avoid leaving practice files behind.

## Important lines explained
- `with path.open("w", encoding="utf-8") as file:` closes the handle even on failure, but overwrites existing content.
- `path.open("a", encoding="utf-8")` preserves existing content and adds new text.
- `Path(__file__).parent / "sample.txt"` locates a file relative to this script, not the shell's current directory.

## Run
Run `python lesson-13-files/13_files.py` from the repository root. The reference uses a temporary directory so no output file is committed.

Expected output:
```text
Lines: 3
First: api
Last: cache
Missing file handled
```

Read [DIY](diy.md) and [reference code](13_files.py). **Trade-off:** Avoid writing over important files; use temporary locations for practice. CSV, JSON and YAML are covered in Lesson 14.
