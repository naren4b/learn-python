# Day 9: Do it yourself

Run `bash diy.sh` from the repository root, edit `lab/app.py`, and execute `python lab/app.py` after saving.

## Pseudocode
```text
SET raw input text containing comma-separated names and spaces
TRIM surrounding spaces and CONVERT to lowercase
SPLIT text into a list using commas
PRINT the first and last element
PRINT number of elements
JOIN elements with ' | '
CHECK whether db occurs in the list
```

## Your Exercise
1. Assign `raw = "  API,DB,Cache  "`.
2. Remove surrounding whitespace with `strip()`, then convert to lowercase.
3. Split on commas and print the first and last service.
4. Print how many services there are.
5. Join them using `" | "` and print the result.
6. Check whether `"db"` exists in the list.

Optional: change the input to `"  API, DB, Cache  "` (spaces after commas) and figure out how to trim each element.

Read [reference code](09_strings.py) only if stuck. No external requirements; do not commit local files.
