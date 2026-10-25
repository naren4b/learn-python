"""Lesson 20: execute Bash and parse JSON output into a dict."""

import json
import subprocess
from pathlib import Path


def main() -> None:
    script = Path(__file__).with_name("status.sh")
    result = subprocess.run(
        ["bash", str(script)],
        capture_output=True,
        text=True,
        check=True,
        timeout=10,
    )
    status = json.loads(result.stdout)
    print("Parsed:", status)
    print(f"Service: {status['service']}, status: {status['status']}")


if __name__ == "__main__":
    main()
