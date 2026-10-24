# Day 8: Do it yourself

From the repository root, run `bash diy.sh` to clear both files and edit the ignored `lab/app.py`. Then run `python lab/app.py`.

## Pseudocode
```text
CREATE a tuple with server name and CPU count
PRINT server name using indexing
CREATE two sets of availability zones
CALCULATE intersection and union
PRINT sorted results and unique item count
```

## Your Exercise
1. Create `server = ("api", 8)`; print the name using indexing.
2. Create `zones_a = {"east", "north", "east"}` and `zones_b = {"east", "south", "west"}`.
3. Print how many unique values are in `zones_a`.
4. Print common zones using intersection (`&`).
5. Print all distinct zones using union (`|`).
6. Use `sorted()` when printing sets, so results have a predictable order.

Optional: Try assigning to `server[1]` and explain the error.

Open [reference code](08_tuples_sets.py) only if stuck.
