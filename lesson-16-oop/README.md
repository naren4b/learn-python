# Lesson 16 — Classes and OOP

## Goal
Create objects using classes, constructors, attributes and methods.

## Basic example

```python
class Server:
    def __init__(self, name, port):
        self.name = name
        self.port = port

    def describe(self):
        return f"{self.name}:{self.port}"

server = Server("api", 8080)
print(server.describe())
```

Output: `api:8080`

## Important syntax

- `class Server` defines a class; `Server(...)` constructs an object.
- `__init__` initializes instance attributes.
- `self` refers to the current instance.
- `self.name` stores a value on that instance.
- An instance method accesses object data through `self`.
- `super()` calls methods inherited from a parent class.
- `@dataclass` generates boilerplate for classes that mainly hold data.

See [DIY](diy.md) and [reference code](16_oop.py). No external dependencies.

## Official references

[Python classes](https://docs.python.org/3.12/tutorial/classes.html) · [dataclasses](https://docs.python.org/3.12/library/dataclasses.html) · [PEP 8](https://peps.python.org/pep-0008/).
