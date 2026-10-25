# Lesson 5: loops

total = 0
# Key step: the following statement creates or updates a value used below.
for number in range(1, 6):
    total += number
print(f"Total: {total}")

count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Done")

# enumerate returns (index, value) pairs; start=1 numbers from one.
services = ["api", "db", "cache"]
for line_number, service in enumerate(services, start=1):
    print(f"{line_number}: {service}")
