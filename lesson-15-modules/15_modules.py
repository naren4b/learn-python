"""Lesson 15: importing a function from a sibling module."""

from helpers import greet


def main() -> None:
    print(greet("api"))


# Importing this module won't execute main().
if __name__ == "__main__":
    main()
