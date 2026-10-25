# Lesson 13: Simple text file handling

Learn to read, write and inspect local text files. Start with `Path` for filenames and `with` to close open files automatically.

## 1. Read a local file

```python
from pathlib import Path

path = Path("hello.txt")
with path.open("r", encoding="utf-8") as file:
    print(file.read())
```

The relative path is resolved from the directory in which you run Python. The file must exist.

## 2. Write, then read

```python
from pathlib import Path

path = Path("hello.txt")
with path.open("w", encoding="utf-8") as file:
    file.write("I am system")

with path.open("r", encoding="utf-8") as file:
    print(file.read())
```

`w` overwrites the file. Use `a` instead if you want to append text.

## 3. Find ERROR lines in a log

```python
from pathlib import Path

path = Path("application.log")

with path.open("r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        if "ERROR" in line:
            print(line_number, line.strip())
```

`enumerate(..., start=1)` provides human-friendly line numbers. `strip()` removes the trailing newline and surrounding whitespace. Processing the file line by line avoids reading the entire file into memory.

## Important syntax

- `Path("file.txt")`: creates a path object.
- `path.open("r", encoding="utf-8")`: opens a UTF-8 text file for reading.
- `with ... as file:`: closes the file when the block ends.
- `file.read()`: reads all remaining text.
- `for line in file:`: reads one line at a time.
- `FileNotFoundError`: raised if a file opened with `r` does not exist.

Both `pathlib` and `tempfile` are Python standard-library modules; no pip installation is needed. The [reference program](13_files.py) also demonstrates a temporary workspace and missing-file handling. Try the [DIY exercise](diy.md).

## Official references

- [Python pathlib](https://docs.python.org/3.12/library/pathlib.html)
- [Python input/output and reading files](https://docs.python.org/3.12/tutorial/inputoutput.html#reading-and-writing-files)
- [Python io](https://docs.python.org/3.12/library/io.html)
- [Python tempfile](https://docs.python.org/3.12/library/tempfile.html)

Import organization and PEP 8 naming are covered in Lesson 15; see [Python import system](https://docs.python.org/3.12/reference/import.html) and [PEP 8](https://peps.python.org/pep-0008/).
