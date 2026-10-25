"""Lesson 17: iterators and generators."""


def count_up_to(limit: int):
    for value in range(1, limit + 1):
        yield value  # Return an item and suspend until next requested.


if __name__ == "__main__":
    for value in count_up_to(3):
        print(value)

    services = iter(["api", "db"])
    print(next(services))
    print(next(services))

    for name, port in zip(["api", "db"], [8080, 5432]):
        print(name, port)
