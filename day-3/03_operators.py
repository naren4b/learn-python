# Day 3: arithmetic, comparisons and logic

price = 100
discount = 20
stock = 5
member = True

final_price = price - price * discount / 100
discount_allowed = member and stock > 0
is_even = 7 % 2 == 0

print(f"Final price: {final_price:.2f}")
print(f"Discount allowed: {discount_allowed}")
print(f"Even number: {is_even}")
print(f"Remainder: {10 % 3}")
