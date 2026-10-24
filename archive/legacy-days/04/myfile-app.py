with open("res/data.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("This is the third line.\n")

file_data = open("res/data.txt", "r").read()
print(file_data)
# File is opened and read without using 'with' statement means it is not automatically closed.

print(type(file_data))
