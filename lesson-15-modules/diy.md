# Lesson 15 DIY

Use the ignored `lab/` directory for practice.

## Your Exercise

1. Create `lab/helpers.py` containing a function `greet(name)` that returns a greeting.
2. In `lab/app.py`, use `from helpers import greet` and call it.
3. Change the code to `import helpers` and call `helpers.greet(...)`.
4. Print `__name__` in each file to observe how direct execution differs from importing.

Optional: Inspect `sys.path`. No third-party dependencies.

## Pseudocode

```text
DEFINE a function in a helper module
IMPORT it from a second script
CALL it and print output
COMPARE direct module import and specific name import
```
