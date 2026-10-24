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

## Import syntax quick reference

| Syntax | Meaning |
| --- | --- |
| `import pathlib` | Import a module; call `pathlib.Path(...)`. |
| `from pathlib import Path` | Bring just `Path` into the current namespace. |
| `import datetime as dt` | Alias a module. |
| `from pathlib import Path as FilePath` | Alias an imported name. |
| `from math import sqrt, pi` | Import selected names. |
| `from math import *` | Import many public names; avoid due to namespace collisions. |
| `from helpers import greet` | Absolute import: find the top-level `helpers` module on the import search path. |
| `from .helpers import greet` | Explicit relative import: find `helpers` in the current package. |

### Absolute versus relative imports

For a package like this:

```text
project/
├── main.py
└── myapp/
    ├── __init__.py
    ├── helpers.py
    └── service.py
```

In `myapp/service.py`, both forms can be useful, but they refer to different locations:

```python
from myapp.helpers import greet  # Absolute: explicitly named package.
from .helpers import greet       # Relative: same package as service.py.
```

By contrast, `from helpers import greet` searches for a **top-level** `helpers` module, not specifically `myapp/helpers.py`. Run package code using `python -m myapp.service` from the project root; directly running `python myapp/service.py` normally breaks relative imports because there is no established package context.

### Python naming conventions (PEP 8)

- Classes: `PascalCase` (e.g. `FileManager`).
- Functions, methods, variables and modules: `snake_case` (e.g. `read_text_file`, `file_manager.py`).
- Constants: `UPPER_SNAKE_CASE` (e.g. `MAX_RETRIES`).
- Internal-use names: leading underscore (e.g. `_parse_line`).
- Special methods: double underscores (e.g. `__init__`).

See [PEP 8](https://peps.python.org/pep-0008/). Imports and packages are revisited in Lesson 15.
