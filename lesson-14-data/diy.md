# Lesson 14 — DIY

Use `bash diy.sh` and your ignored `lab/app.py`. Start with JSON; proceed to CSV and YAML when ready.

## Pseudocode

```text
CREATE one dictionary representing a service
WRITE it as JSON, then READ it and PRINT the name
WRITE two service rows as CSV, then READ and PRINT the names
WRITE the service as YAML, then READ and PRINT the name
HANDLE a missing file or malformed document
```

## Your Exercise

1. Create `services.json` with `name`, `port`, and `enabled`; read it using `json.load()`.
2. Write two rows to `services.csv` with `csv.DictWriter`; read using `csv.DictReader`.
3. Write and read `services.yaml` with `yaml.safe_dump()` and `yaml.safe_load()`.
4. Optional: catch `FileNotFoundError` and a format-specific parse error.

See [README](README.md) for minimal examples and [reference](14_data_formats.py) if needed.
