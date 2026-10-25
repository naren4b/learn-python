# Lesson 20 — DIY

Use the existing `lab/app.py`.

## Your Exercise

1. Run the current Python interpreter with `--version` using `subprocess.run()`.
2. Set `capture_output=True`, `text=True`, `check=True` and `timeout=10`.
3. Print its stdout/stderr and return code.
4. Run an invalid command argument and catch `subprocess.CalledProcessError`.

Avoid `shell=True`. Refer to [Lesson 19](../lesson-19-cli/README.md) for environment variables.
