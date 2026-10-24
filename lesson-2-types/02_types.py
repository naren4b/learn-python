# Lesson 2: values have types inferred from their assignments.
city = "Chennai"
age = 45
price = 12.5
ready = True

# type(value).__name__ displays a readable type name.
for value in (city, age, price, ready):
    print(f"{value}: {type(value).__name__}")

# An f-string can evaluate expressions inside braces.
print(f"Next year: {age + 1}")
