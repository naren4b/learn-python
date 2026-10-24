# Day 10: Do it yourself

Run `bash diy.sh` from the repository root, then `python lab/app.py` after saving.

## Pseudocode
```text
STORE a list of numbers
SORT without modifying the original list
BUILD a list with doubled values
BUILD a filtered list of values greater than ten
BUILD a dictionary mapping names to lengths
BUILD a set to remove duplicates
PRINT results
```

## Your Exercise
1. Start with `numbers = [20, 5, 30, 10, 5]`.
2. Print a sorted copy of the numbers.
3. Use a list comprehension to double each value.
4. Use another comprehension to keep only values greater than 10.
5. Make `names = ["api", "worker"]` and a dictionary comprehension mapping names to their lengths.
6. Remove duplicate numbers using a set comprehension and print them sorted.

Optional: Print the first three elements of the sorted copy using slicing. The full answer is in [reference code](10_comprehensions.py) if needed.
