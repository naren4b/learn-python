# Day 9: strings and their methods

raw = "  API,DB,Cache  "
services = raw.strip().lower().split(",")

print(f"First: {services[0]}")
print(f"Last: {services[-1]}")
print(f"Count: {len(services)}")
print(f"Joined: {' | '.join(services)}")
print(f"Has db: {'db' in services}")
