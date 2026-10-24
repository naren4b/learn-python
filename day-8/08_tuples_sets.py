# Day 8: tuples and sets

server = ("api", 8)
zones_a = {"east", "north", "east"}
zones_b = {"east", "south", "west"}

print(f"Server: {server[0]}")
print(f"Unique zones: {len(zones_a | zones_b) - 1}")
print(f"Common zones: {sorted(zones_a & zones_b)}")
print(f"All zones: {sorted(zones_a | zones_b)}")
