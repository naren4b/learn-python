# Create a list of fruits (allows duplicates and is changeable) decalred in [square brackets]
fruit_list = [
    "mango",
    "banana",
    "apple",
]
# Add an element
fruit_list.append("orange")
# Output: ['apple', 'banana', 'cherry', 'apple', 'orange']

print(f"My Fruits List: {fruit_list}\n")

print(f"Number of fruits: {len(fruit_list)}\n")
print("Print each fruit in the list:")
for fruit in fruit_list:
    print(fruit)
print()
# Access an element by index
print("Accessing element at index 1:")
print(fruit_list[1])  # Output: banana
