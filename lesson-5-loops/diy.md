# Day 5: Do it yourself

From the repository root, run `bash diy.sh` to empty `lab/app.py` and `lab/requirements.txt` and open `app.py` in `vi`. After saving, run `python lab/app.py`.

## Pseudocode
```text
SET total to zero
FOR each number from 1 through 5
    ADD number to total
PRINT total
SET count to 3
WHILE count is greater than zero
    PRINT current count
    DECREASE count by one
PRINT Done
```

## Exercise
1. Use `for` and `range()` to sum the integers from 1 through 5.
2. Print the total once, after the loop.
3. Use `while` to print a countdown from 3 to 1.
4. Print `Done` once after the countdown.
5. Change the sum's upper limit to 10 and check the new total.

Use [the reference code](05_loops.py) only if stuck. Do not commit your local practice files.

## Optional: enumerate

Loop through `["api", "db", "cache"]` with `enumerate(..., start=1)` and print the position and the service name.
