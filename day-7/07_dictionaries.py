# Day 7: dictionaries

server = {"name": "api", "cpu": 4}
print(f"Server: {server['name']}")

server["cpu"] = 8
print(f"CPU: {server['cpu']}")
print(f"Region: {server.get('region', 'unknown')}")

for key, value in server.items():
    print(f"{key}: {value}")
