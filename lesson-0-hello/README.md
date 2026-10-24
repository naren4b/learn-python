# Day 0: Run Python with Podman

## Objective
Save a Python file in a text editor and run it with Python 3.12.14 inside Podman.

## Remember
- Run commands from the root of this repository in WSL.
- Podman uses the fixed image `docker.io/library/python:3.12.14-slim-bookworm`.
- `-v "$PWD:/work"` makes the current folder visible inside the container.
- `-w /work` sets the working folder inside the container.
- `--rm` removes the temporary container after execution.
- Python is installed in the container. No local Python installation is required.

## Files
- `00_hello.py`: first runnable program
- `requirements.txt`: no external packages needed

## Run

```bash
cd /mnt/c/code/personal/learn-python
pwd
podman run --rm docker.io/library/python:3.12.14-slim-bookworm python --version
podman run --rm -v "$PWD:/work" -w /work docker.io/library/python:3.12.14-slim-bookworm python lesson-0-hello/00_hello.py
```

Expected:

```text
Python 3.12.14
Hello, Python!
```

Use your existing repository checkout. Do not create a second working directory.

## Practice
Open `lesson-0-hello/00_hello.py` in Notepad, change the greeting, save the file, and run the command again.

## Trade-off
A fixed Podman image gives consistent Python versions across machines. Local Python is faster to launch but may use a different version. Use Podman for reproducible exercises.

## Important line notes

- `print(...)` writes text to the terminal.
