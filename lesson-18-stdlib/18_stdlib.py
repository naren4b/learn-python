"""Lesson 18: standard-library examples."""

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def main():
    statuses = [200, 500, 200, 404, 500, 200]
    counts = Counter(statuses)  # Count each occurrence.
    print("Counts:", counts)
    print("Most common:", counts.most_common(1))
    print("UTC:", datetime.now(timezone.utc).isoformat())
    print("services.yaml exists:", Path("services.yaml").exists())


if __name__ == "__main__":
    main()
