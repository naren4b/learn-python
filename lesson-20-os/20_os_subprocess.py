"""Lesson 20: safely execute external processes."""

import subprocess
import sys


def main() -> None:
    result = subprocess.run(
        [sys.executable, "--version"],  # Executable and arguments are separate items.
        capture_output=True,  # Capture stdout and stderr.
        text=True,  # Decode output to str.
        check=True,  # Raise CalledProcessError on nonzero exit.
        timeout=10,  # Raise TimeoutExpired if the command hangs.
    )
    print("Version:", (result.stdout or result.stderr).strip())
    print("Return code:", result.returncode)


if __name__ == "__main__":
    main()
