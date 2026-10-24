# Day 2: common Python value types

city = "Chennai"
age = 45
price = 12.5
ready = True

for value in (city, age, price, ready):
    print(f"{value}: {type(value).__name__}")

print(f"Next year: {age + 1}")
