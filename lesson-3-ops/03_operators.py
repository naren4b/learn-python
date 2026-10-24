# Lesson 3: arithmetic, comparison and logical operators.
price = 100
discount = 20
stock = 5
member = True

# Divide by 100 to interpret discount as a percentage.
final_price = price - price * discount / 100
# Both membership and availability must be true.
discount_allowed = member and stock > 0
# % is remainder; == checks equality.
is_even = 7 % 2 == 0

# :.2f formats a number to two decimal places.
print(f"Final price: {final_price:.2f}")
print(f"Discount allowed: {discount_allowed}")
print(f"Even number: {is_even}")
print(f"Remainder: {10 % 3}")
