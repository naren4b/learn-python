# Day 3: Do it yourself

Use your ignored local practice directory in WSL. The commands reset both scratch files to empty.

```bash
mkdir -p /mnt/c/code/personal/learn-python/lab
cd /mnt/c/code/personal/learn-python/lab
: > app.py
: > requirements.txt
vi app.py
python app.py
```

## Pseudocode

```text
SET price, discount, stock, member
CALCULATE discounted price
CHECK membership AND stock availability
CHECK whether 7 is even
FIND remainder when 10 is divided by 3
PRINT each result
```

## Exercise

Write a program that:
1. Sets `price = 100`, `discount = 20`, `stock = 5` and `member = True`.
2. Calculates and prints the final price after the discount.
3. Uses `and` to check if the customer is a member and stock is greater than zero.
4. Prints whether `7` is even using `%`.
5. Prints the remainder of `10 % 3`.

Change `stock` to `0` and predict which result changes. Run it again.

No packages are required. Do not commit `lab/app.py`. Open [the reference code](03_operators.py) only if stuck.
