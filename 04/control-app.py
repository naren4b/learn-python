print("Hello from 04/app.py")

todos = ["a", "b", "c"]

for i in todos:
    print(f"{i}.")
    # lets pick one todo
    if i == "b":
        print(f"\n Picked todo: {i}\n")
        break

