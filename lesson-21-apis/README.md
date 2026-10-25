# Lesson 21 — HTTP APIs with Python

## Goal
Make HTTP requests, check status codes, parse JSON into Python dictionaries, and handle errors safely.

## Standard-library approach: urllib

```python
import json
from urllib.request import urlopen

with urlopen("https://httpbin.org/json", timeout=10) as response:
    data = json.load(response)
    print(response.status)
    print(type(data).__name__)
```

## Key concepts

| Concept | Meaning |
| --- | --- |
| GET | Fetch a resource |
| POST | Submit data to a service |
| HTTP status | 2xx success, 4xx client error, 5xx server error |
| `timeout=10` | Avoid waiting indefinitely |
| `json.load(response)` | Parse JSON from a file-like response |
| `urllib.error.HTTPError` | Error returned with an HTTP status |
| `urllib.error.URLError` | Connection, DNS or related errors |

Always validate expected JSON keys before using them. Do not send credentials in URLs or print access tokens.

`urllib` is built into Python. The third-party `requests` package is a practical alternative that we can compare next.

[DIY](diy.md) · [Reference](21_apis.py) · [Official urllib docs](https://docs.python.org/3.12/library/urllib.request.html) · [JSON docs](https://docs.python.org/3.12/library/json.html).
