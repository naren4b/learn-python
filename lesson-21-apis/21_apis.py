"""Lesson 21: HTTP GET with timeout, JSON decoding and error handling."""

import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def main() -> None:
    try:
        with urlopen("https://httpbin.org/json", timeout=10) as response:
            data = json.load(response)  # JSON object -> Python dict.
            print("HTTP status:", response.status)
            print("JSON type:", type(data).__name__)
            print("Keys:", list(data))
    except HTTPError as error:
        print("HTTP error:", error.code)
    except URLError as error:
        print("Network error:", error.reason)


if __name__ == "__main__":
    main()
