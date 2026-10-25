# Lesson 14 — CSV, JSON and YAML

Use Python to read and write three common structured file formats. Start with **JSON**, then CSV, then YAML.

| Format | Typical use | Python module | Extra installation |
| --- | --- | --- | --- |
| JSON | APIs, structured configuration | `json` | None |
| CSV | Tabular records, reports | `csv` | None |
| YAML | Human-readable configuration | `yaml` (PyYAML) | `PyYAML` |

## 1. JSON — read a dictionary

Given `services.json`:

```json
{"name": "api", "port": 8080, "enabled": true}
```

```python
import json
from pathlib import Path

with Path("services.json").open("r", encoding="utf-8") as file:
    service = json.load(file)  # Convert JSON into Python objects.

print(service["name"])
```

Use `json.dump(data, file, indent=2)` to write a file; `json.loads(text)` to parse a string.

## 2. CSV — rows with named columns

Given `services.csv`:

```csv
name,port
api,8080
db,5432
```

```python
import csv
from pathlib import Path

with Path("services.csv").open("r", encoding="utf-8", newline="") as file:
    for row in csv.DictReader(file):
        print(row["name"], row["port"])
```

`DictReader` uses the header as keys. CSV values are strings; convert `port` with `int()` when needed. Write rows using `csv.DictWriter`.

## 3. YAML — configuration files

Given `services.yaml`:

```yaml
name: api
port: 8080
enabled: true
```

```python
import yaml
from pathlib import Path

with Path("services.yaml").open("r", encoding="utf-8") as file:
    service = yaml.safe_load(file)  # Use safe_load for input files.

print(service["name"])
```

PyYAML is an external package. Install it in an isolated environment from [requirements.txt](requirements.txt). Use `yaml.safe_dump(data, file)` to write.

## Run the complete commented reference

```bash
uv venv
uv pip install -r lesson-14-data/requirements.txt
.venv/bin/python lesson-14-data/14_data_formats.py
```

The reference creates temporary example files, reads them back and cleans up automatically.

## Important distinctions

- `load(file)` reads from a file handle; `loads(text)` reads from a string (for JSON).
- `dump(data, file)` writes to a file; `dumps(data)` returns a string (for JSON).
- JSON `true` becomes Python `True`; JSON `null` becomes `None`.
- Use `with Path(...).open(...)` for explicit file handling, and catch parse errors when processing untrusted files.

[Your exercise](diy.md) · [Reference code](14_data_formats.py)

## JSON, YAML and CSV: updating existing data

| Operation | JSON | YAML | CSV |
| --- | --- | --- | --- |
| Load data | `json.load(file)` | `yaml.safe_load(file)` | `csv.DictReader(file)` |
| Add key to dictionary | `data["key"] = value` | Same Python dictionary operation | Same for a row dictionary |
| Add record to list | `data.append(record)` | Same Python list operation | `writer.writerow(record)` |
| Save changes | `json.dump(data, file)` | `yaml.safe_dump(data, file)` | `csv.DictWriter(file, ...)` |
| Append directly to file | Generally no | Generally no | Yes, using `"a"` |

**Remember:** Dictionaries add or update keys; lists use `.append()`. For JSON and YAML, normally **load → modify → write the entire updated object**. For CSV, append rows using `"a"` and avoid writing the header again.

## Working pattern: read → parse → modify → save

Use the parsed **Python objects**, not raw file text:

1. Read the file and parse it into Python objects.
2. Modify a `dict` with `data["key"] = value` or `update()`, or modify a `list` with `append()`.
3. Write the complete updated object back to the file.

| Format | Parsed data | Updating files |
| --- | --- | --- |
| JSON | Dictionary, list, or another JSON-compatible value | `json.load()` → modify → `json.dump()` |
| YAML | Dictionary, list, or another supported YAML value | `yaml.safe_load()` → modify → `yaml.safe_dump()` |
| CSV | Rows, commonly represented as dictionaries by `DictReader` | Read/modify/rewrite, **or append rows directly** with `DictWriter` and `"a"` |

Use separate read and write file handles. Beware that opening with `"w"` replaces the existing file, and repeated appends may create duplicate records. For large CSV files, process rows incrementally.

## Official references

[Python json](https://docs.python.org/3.12/library/json.html) · [Python csv](https://docs.python.org/3.12/library/csv.html) · [PyYAML documentation](https://pyyaml.org/wiki/PyYAMLDocumentation) · [pathlib](https://docs.python.org/3.12/library/pathlib.html)
