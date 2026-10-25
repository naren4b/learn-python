# Lesson 18 — Standard library

Python ships with useful modules; no additional installation is needed.

| Module | Purpose |
| --- | --- |
| `collections.Counter` | Count repeated values |
| `datetime` | Handle dates and times |
| `pathlib.Path` | Manipulate filesystem paths |
| `statistics` | Calculate numeric summaries |
| `re` | Match text patterns |

Example:

```python
from collections import Counter
statuses = [200, 500, 200, 404, 500, 200]
print(Counter(statuses).most_common(1))
```

**Notes:** Use timezone-aware dates. Prefer `in` over regular expressions for simple substring checks.

[DIY](diy.md) · [Reference](18_stdlib.py) · [Official standard library docs](https://docs.python.org/3.12/library/index.html)
