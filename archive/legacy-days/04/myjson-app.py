import json

print("Read a Json file and print the data")


with open("res/data.json", "r") as f:
    data = json.load(f)

address = data.get("address", {})
print("Address:", address)

print("json list")

with open("res/students.json", "r") as s:
    students = json.load(s)

for student in students:
    print(student)
