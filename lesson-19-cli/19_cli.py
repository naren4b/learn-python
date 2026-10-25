"""Lesson 19: parse positional and optional CLI arguments."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Describe a service")
    parser.add_argument("service", help="Service name")  # Required positional argument.
    parser.add_argument("--port", type=int, default=8080)  # Optional integer.
    args = parser.parse_args()
    print(f"{args.service}:{args.port}")


if __name__ == "__main__":
    main()
