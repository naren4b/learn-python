# Lesson 21 — DIY

Use `lab/app.py`.

## Your Exercise

1. Perform an HTTP GET request to `https://httpbin.org/json` using `urllib.request.urlopen` and a timeout.
2. Print the HTTP status code.
3. Parse the response using `json.load(response)` and print the Python type.
4. Print one available key from the parsed dictionary.
5. Catch `urllib.error.HTTPError` and `urllib.error.URLError`.

Requires an internet connection. Do not put secrets in test URLs.
