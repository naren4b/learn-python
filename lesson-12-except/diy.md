# Lesson 12 DIY

Use root `bash diy.sh` and write your own version in `lab/app.py`.

## Pseudocode
```text
DEFINE a function that converts a text value to a number
TRY to divide 100 by the number
CATCH an invalid number
CATCH division by zero
ON success, show the result
ALWAYS print a completion message
TEST a valid number, invalid text, and zero
```

## Your Exercise
1. Write `safe_divide(raw)` to compute `100 / int(raw)`.
2. Catch `ValueError` and `ZeroDivisionError` separately.
3. Use `else` to print the result on success.
4. Use `finally` to print `"Cleanup complete"`.
5. Call the function with `"20"`, `"abc"` and `"0"`.

Optional: Raise `ValueError` yourself when input is negative.
