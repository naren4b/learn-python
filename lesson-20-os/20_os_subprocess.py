"""Lesson 20: environment settings and safe subprocess calls."""

import os
import subprocess
import sys
from pathlib import Path


def main() -> None:
    env_name = os.getenv("APP_ENV", "dev")
    print("Environment:", env_name)
    print("Working directory:", Path.cwd())

    result = subprocess.run(
        [sys.executable, "--version"],  # Avoid shell commands for simple executions.
        capture_output=True,
        text=True,
        check=True,  # Raise if the command fails.
        timeout=10,  # Avoid hanging indefinitely.
    )
    print("Version:", (result.stdout or result.stderr).strip())
    print("Return code:", result.returncode)


if __name__ == "__main__":
    main()
