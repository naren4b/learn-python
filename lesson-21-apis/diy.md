# Lesson 21 — DIY

Use `lab/app.py`.

## Your Exercise

1. Make an HTTP GET request with `urllib.request.urlopen()`, a timeout, and `json.load()`.
2. Add **HTTP Basic Auth** using a `Request` with the Authorization header. Read username/password from environment variables; do not hardcode or print real credentials.
3. Simulate **pagination** using page-number arguments; collect all returned items in a list until a page is empty or the API says there is no next page.
4. Handle `HTTPError` (including 401 Unauthorized and 429 rate-limit responses) and `URLError`.
5. Optional: inspect an API's `next` cursor/URL rather than assuming page numbers.

Reference endpoints, authentication safety, and a pagination example are explained in [README](README.md).
