# Lesson 15 — Modules, packages and imports

## Goal
Understand how Python finds and imports code from files and packages.

## Import styles

| Syntax | Meaning |
| --- | --- |
| `import math` | Import the module; use `math.sqrt(16)` |
| `from math import sqrt` | Import one name; use `sqrt(16)` |
| `import math as m` | Give the module an alias |
| `from helpers import greet` | Absolute import: locate top-level `helpers` on Python's import path |
| `from .helpers import greet` | Relative import: locate `helpers` inside the current package |
| `from math import *` | Wildcard import; generally avoid |

## Small local example

Files in the same directory:

```text
lesson-15-modules/
├── 15_modules.py
├── helpers.py
├── README.md
├── diy.md
└── requirements.txt
```

```python
from helpers import greet

print(greet("api"))
```

In `helpers.py`, `greet` is a normal function. Python searches `sys.path` for imports. The current script's directory is normally on that search path.

## Package imports

Given `myapp/service.py` and `myapp/helpers.py`:

- `from myapp.helpers import greet` uses an absolute package path.
- `from .helpers import greet` uses the current package (`.`), and requires package context.
- From the project root, `python -m myapp.service` establishes that context; running `myapp/service.py` directly normally does not.

## Important lines explained

- `if __name__ == "__main__":` runs the example only when the file is executed, not when imported.
- `from helpers import greet` imports one function from `helpers.py`.
- `import sys; print(sys.path)` helps diagnose module lookup.
- Standard-library modules need no installation. Third-party modules are installed in the selected Python environment.

## Naming conventions (PEP 8)

Classes use `PascalCase`; functions, variables and module filenames use `snake_case`; constants use `UPPER_SNAKE_CASE`.

## Run

```bash
python lesson-15-modules/15_modules.py
```

Expected: `Hello, api`

[Exercise](diy.md) · [Reference](15_modules.py) · [Official import system](https://docs.python.org/3.12/reference/import.html) · [Official modules tutorial](https://docs.python.org/3.12/tutorial/modules.html) · [PEP 8](https://peps.python.org/pep-0008/).
