# Day 11: Do it yourself

From the repository root run `bash diy.sh`, edit `lab/app.py`, then run `python lab/app.py`.

## Pseudocode
```text
DEFINE function to multiply unit price by quantity (quantity defaults to one)
CALL it with keyword arguments
DEFINE function accepting any number of labels
RETURN label count
DEFINE function accepting named server attributes
RETURN region if present, otherwise unknown
USE a lambda to double a number
PRINT the results
```

## Your Exercise
1. Define `total_price(price, quantity=1)` and return the multiplication.
2. Call it with `price=100, quantity=3` and format the result to two decimal places.
3. Define `count_labels(*labels)` and return how many labels were supplied.
4. Define `get_region(**attributes)` and return the `region` value or `"unknown"`.
5. Use `lambda` to double `4` and print the result.
6. Optional: Add `-> float` or `-> int` return type hints to suitable functions.

Use [reference code](11_functions.py) only if stuck. No packages required. Don't commit local practice files.
