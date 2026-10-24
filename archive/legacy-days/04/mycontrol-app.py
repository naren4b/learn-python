print("Hello from 04/app.py")

todos = ["a", "b", "c"]

for i in todos:
    print(f"{i}.")
    # lets pick one todo
    if i == "b":
        print(f"\n Picked todo: {i}\n")
        break

while True:
    print("In while loop")
    break

i = 8

while i > 0:
    print(f"Countdown: {i}")
    i -= 1


def my_recursive_function(n):
    if n <= 0:
        print("Base case reached")
        return
    print(f"Recursion level: {n}")
    my_recursive_function(n - 1)


my_recursive_function(5)
