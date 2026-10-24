# Day 4: Do it yourself

Use WSL. Run the root [diy.sh](../diy.sh) with `bash diy.sh` from the repository root. It **empties both local scratch files** and opens `lab/app.py` in `vi`. After saving and exiting, run `python lab/app.py` from the repository root.

## Pseudocode

```text
DEFINE function discounted_price(price, discount)
    CALCULATE price after percentage discount
    RETURN calculated price

DEFINE function in_stock(stock, quantity)
    RETURN whether stock covers requested quantity

SET price = 200, discount = 20, stock = 5, quantity = 2
CALL discounted_price and store its result
MULTIPLY discounted unit price by quantity
CALL in_stock and store its result
PRINT discounted unit price, total and stock check
```

## Your exercise

1. Write the two functions `discounted_price(price, discount)` and `in_stock(stock, quantity)`.
2. Use `return` in both functions, not `print` inside them.
3. Call both functions with the values above. Display the unit price and order total to two decimal places, plus the stock-check boolean.
4. Change `quantity` to `6`. What changes? Does the total still calculate?

No packages required. Do not commit `lab/app.py`. Check [reference code](04_functions.py) only if stuck.
