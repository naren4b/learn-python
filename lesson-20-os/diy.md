# Lesson 20 — DIY

Use your local `lab/app.py`.

## Your Exercise

1. Read `APP_ENV` with `os.getenv("APP_ENV", "dev")`.
2. Print the current working directory with `Path.cwd()`.
3. Run `[sys.executable, "--version"]` using `subprocess.run()` with `capture_output=True`, `text=True`, `check=True`, and `timeout=10`.
4. Print the captured output and process return code.

Try `APP_ENV=prod python lab/app.py` and compare it to the default.

## Pseudocode

Read setting; locate working directory; run safe subprocess; inspect output and exit status.
