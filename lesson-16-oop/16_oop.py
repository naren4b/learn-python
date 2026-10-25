"""Lesson 16: creating classes and objects."""


class Server:
    def __init__(self, name: str, port: int):
        # Save instance-specific values.
        self.name = name
        self.port = port

    def describe(self) -> str:
        return f"{self.name}:{self.port}"


if __name__ == "__main__":
    first = Server("api", 8080)
    second = Server("cache", 6379)
    print(first.describe())
    print(second.describe())
