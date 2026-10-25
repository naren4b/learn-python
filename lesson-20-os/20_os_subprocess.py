"""Lesson 20: run Docker and convert JSON Lines into Python dictionaries.

Why subprocess.run() instead of os.system() or os.exec*()?
- os.system() runs a shell command but only returns its exit status.
- os.exec*() replaces the current Python process when successful.
- subprocess.run() lets Python continue and capture stdout/stderr.
"""

import json
import subprocess


def main() -> None:
    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "{{json .}}"],
            capture_output=True,  # Collect stdout/stderr for parsing.
            text=True,            # Decode output as strings.
            check=True,           # Raise on a nonzero exit code.
            timeout=10,
        )
    except (FileNotFoundError, subprocess.CalledProcessError,
            subprocess.TimeoutExpired) as error:
        print(f"Could not list Docker containers: {error}")
        return

    # docker ps --format '{{json .}}' emits one JSON object per line.
    containers = [json.loads(line) for line in result.stdout.splitlines()]
    print(f"Running containers: {len(containers)}")
    for container in containers:
        print(container.get("Names"), container.get("Status"))


if __name__ == "__main__":
    main()
