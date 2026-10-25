"""Lesson 14: CSV, JSON and YAML using temporary files."""

import csv
import json
from pathlib import Path
from tempfile import TemporaryDirectory

import yaml  # Third-party: PyYAML (see requirements.txt).


def main() -> None:
    service = {"name": "api", "port": 8080, "enabled": True}

    # Temporary files disappear when the context exits.
    with TemporaryDirectory() as folder:
        root = Path(folder)

        json_path = root / "services.json"
        with json_path.open("w", encoding="utf-8") as file:
            json.dump(service, file, indent=2)
        with json_path.open("r", encoding="utf-8") as file:
            loaded_json = json.load(file)
        print(f"JSON: {loaded_json['name']}")

        csv_path = root / "services.csv"
        with csv_path.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "port"])
            writer.writeheader()
            writer.writerows([
                {"name": "api", "port": 8080},
                {"name": "db", "port": 5432},
            ])
        with csv_path.open("r", encoding="utf-8", newline="") as file:
            rows = list(csv.DictReader(file))
        print(f"CSV: {', '.join(row['name'] for row in rows)}")

        yaml_path = root / "services.yaml"
        with yaml_path.open("w", encoding="utf-8") as file:
            yaml.safe_dump(service, file)
        with yaml_path.open("r", encoding="utf-8") as file:
            loaded_yaml = yaml.safe_load(file)
        print(f"YAML: {loaded_yaml['name']}")


if __name__ == "__main__":
    main()
