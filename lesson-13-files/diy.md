# Lesson 13: DIY

Use `bash diy.sh` from the repository root and edit your local ignored `lab/app.py`.

## Pseudocode
```text
CHOOSE a file under local lab directory
WRITE two lines to it
APPEND one more line without overwriting
READ the contents
SPLIT into lines, count and print first/last
TRY to read a nonexistent file and catch the expected exception
```

## Your Exercise
1. Create a text file under `lab/` containing `api` and `db` on separate lines.
2. Append `cache` on a third line.
3. Read the text and print the line count, first and last entries.
4. Handle `FileNotFoundError` for a missing file.
5. Optional: Use `Path.read_text()` in place of `with open()`.

Do not commit your local practice files. See [reference code](13_files.py) only if needed.
