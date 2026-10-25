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

## Password-based authentication (HTTP Basic Auth)

Some APIs accept a username and password through **HTTP Basic authentication**. Use **HTTPS only**: Base64 encoding is not encryption. Many modern APIs prefer short-lived tokens or OAuth instead.

```python
import base64
import os
from urllib.request import Request, urlopen

username = os.environ["API_USERNAME"]
password = os.environ["API_PASSWORD"]
encoded = base64.b64encode(f"{username}:{password}".encode()).decode()
request = Request(
    "https://httpbin.org/basic-auth/demo/secret",
    headers={"Authorization": f"Basic {encoded}"},
)
with urlopen(request, timeout=10) as response:
    print(response.status)
```

In WSL, set credentials in the shell without committing them to source control. Avoid logging headers or passwords. The demo URL above has public example credentials; replace it with your API endpoint and credentials in the environment.

## Pagination

An API may split a large result into pages. Check its documentation: common forms are `page`/`per_page`, `offset`/`limit`, and opaque cursor/next-link tokens.

Example of *page-number* pagination (adapt keys to the API):

```python
import json
from urllib.parse import urlencode
from urllib.request import urlopen

all_items = []
for page in range(1, 101):  # Safety cap; avoid unbounded loops
    query = urlencode({"page": page, "per_page": 50})
    with urlopen(f"https://api.example.com/items?{query}", timeout=10) as response:
        payload = json.load(response)
    items = payload["items"]  # Assumes an API response containing "items"
    all_items.extend(items)
    if not items or not payload.get("has_more", False):
        break
```

This is a **schema illustration**, not a runnable public endpoint. Follow server-provided `next` URLs/cursors when available; handle HTTP 429 rate limits and retries, and don't assume every API uses `has_more`.

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
