# Day 7: Do it yourself

From the repository root, run `bash diy.sh` to reset and edit your ignored local `lab/app.py`. After saving, run `python lab/app.py`.

## Pseudocode
```text
CREATE a dictionary describing a server
PRINT its name using a key
UPDATE its CPU value
LOOK UP an optional region with a default
FOR each key and value in the dictionary
    PRINT the pair
```

## Your Exercise
1. Create `server = {"name": "api", "cpu": 4}`.
2. Print the server name.
3. Change `cpu` to `8`.
4. Print `region` using `get()` with default `"unknown"`.
5. Iterate through all key-value pairs using `items()` and print each.
6. Add `"region": "eu-central-1"` and observe the change.

Use [reference code](07_dictionaries.py) only if needed. Keep local practice outside Git.
