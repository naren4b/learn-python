# Create a dictionary representing a person's details (key-value pairs)
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "children": {"name": "Bob"},
    "hobbies": ["reading", "traveling", "swimming"],
}


# Access a value using its key
print("Key Values ")
for key in person:
    print(f"{key}: {person[key]}")

print()
# Access nested dictionary value
print(f"Chidren Names: {person["children"]["name"]}")

# Add a new key-value pair
person["profession"] = "Engineer"

print("\nAfter Adding Profession:")
for key in person:
    print(f"{key}: {person[key]}")
