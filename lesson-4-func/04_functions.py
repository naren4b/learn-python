# Lesson 4: reusable functions and return values


# Key step: the following statement creates or updates a value used below.
def discounted_price(price, discount):
    return price - price * discount / 100


def in_stock(stock, quantity):
    return stock >= quantity


price = 200
discount = 20
stock = 5
quantity = 2

unit_price = discounted_price(price, discount)
total = unit_price * quantity
available = in_stock(stock, quantity)

print(f"Unit price after discount: {unit_price:.2f}")
print(f"Order total: {total:.2f}")
print(f"In stock: {available}")
