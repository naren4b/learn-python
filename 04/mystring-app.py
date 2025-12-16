# print(f"{"hello".find("k")}")
url = "https://example.com?name=naren&age=25&city=NYC"
params = url.split("?")[1].split("&")
print(f"URL Parameters: {params}")


url = "https://example.com?name=naren&age=25&city=NYC"
params = url.split("?")[1].split("&")
param_dict = {k: v for k, v in (p.split("=") for p in params)}
print(param_dict)
# {'name': 'naren', 'age': '25', 'city': 'NYC'}

items = ["apple", "banana", "cherry"]
# ❌ Slow: String concatenation in loop
result = ""
for item in items:
    result = result + "-" + item  # Creates new string each time

# ✅ Fast: Use join()
result = "-".join(items)
print(result)  # Output: applebananacherry
