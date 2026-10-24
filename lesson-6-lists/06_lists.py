# Lesson 6: lists

# Key step: the following statement creates or updates a value used below.
latencies = [120, 130, 140]
latencies.append(160)

print(f"First: {latencies[0]}")
print(f"Last: {latencies[-1]}")
print(f"Count: {len(latencies)}")

total = sum(latencies)
average = total / len(latencies)

print(f"Total: {total}")
print(f"Average: {average:.2f}")
