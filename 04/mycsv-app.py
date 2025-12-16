import csv


with open("res/data.csv", "r") as f:
    data = list(csv.reader(f))

for row in data:
    print(row)


# Key Takeaway why list(csv.reader) is used above:
# json.load() → Reads entire file into memory ✅
# csv.reader() → Lazy iterator, reads on demand ❌ (fails if file closed)
# Solution: Always iterate inside the with block or convert to list first
