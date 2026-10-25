"""Lesson 19: CLI inputs via sys and argparse, config via os."""

import argparse
import os
import sys


def main() -> None:
    # sys.argv gives raw strings: argv[0] is the script path.
    print("Raw CLI arguments:", sys.argv[1:])

    parser = argparse.ArgumentParser(description="Describe a service")
    parser.add_argument("service", help="Required positional service name")
    # The env var is a fallback; explicit --port overrides it.
    env_port = int(os.getenv("APP_PORT", "8080"))
    parser.add_argument("--port", type=int, default=env_port)
    args = parser.parse_args()

    print(f"{args.service}:{args.port}")


if __name__ == "__main__":
    main()
