# Day 10: sorting and comprehensions

numbers = [20, 5, 30, 10, 5]
names = ["api", "worker"]

print(f"Sorted: {sorted(numbers)}")
print(f"Doubled: {[n * 2 for n in sorted(numbers)]}")
print(f"Above 10: {[n for n in sorted(numbers) if n > 10]}")
print(f"Name lengths: { {name: len(name) for name in names} }")
print(f"Unique: {sorted({n for n in numbers})}")
