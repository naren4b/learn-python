"""Lesson 20: inspect Docker's JSON Lines output as Python dictionaries."""

import json
import subprocess


def main() -> None:
    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "{{json .}}"],
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.CalledProcessError,
            subprocess.TimeoutExpired) as error:
        print(f"Could not list Docker containers: {error}")
        return

    containers = [json.loads(line) for line in result.stdout.splitlines()]
    print(f"Running containers: {len(containers)}")
    for container in containers:
        print(container.get("Names"), container.get("Status"))


if __name__ == "__main__":
    main()
