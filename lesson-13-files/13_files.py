# Lesson 13: safe text file IO.
from pathlib import Path
from tempfile import TemporaryDirectory


def demonstrate_files() -> None:
    # TemporaryDirectory deletes practice files after the demonstration.
    with TemporaryDirectory() as folder:
        path = Path(folder) / "services.txt"

        # Mode 'w' overwrites the target; encoding is explicit for portability.
        with path.open("w", encoding="utf-8") as stream:
            stream.write("api\ndb\n")

        # Mode 'a' preserves content and appends at the end.
        with path.open("a", encoding="utf-8") as stream:
            stream.write("cache\n")

        # The context manager closes the file, even if reading fails.
        with path.open("r", encoding="utf-8") as stream:
            lines = stream.read().splitlines()

        print(f"Lines: {len(lines)}")
        print(f"First: {lines[0]}")
        print(f"Last: {lines[-1]}")

        try:
            (Path(folder) / "missing.txt").read_text(encoding="utf-8")
        except FileNotFoundError:
            print("Missing file handled")


if __name__ == "__main__":
    demonstrate_files()
