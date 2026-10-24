# Lesson 12: handle expected errors explicitly.


def safe_divide(raw: str) -> None:
    try:
        # int() raises ValueError for text that is not a valid integer.
        divisor = int(raw)
        result = 100 / divisor
    except ValueError:
        # Catch invalid input without masking unrelated bugs.
        print(f"Invalid number: {raw}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        # else executes only if no exception occurred in try.
        print(f"Result: {result:.1f}")
    finally:
        # finally executes after success or a handled failure.
        print("Cleanup complete")


for value in ("20", "abc", "0"):
    safe_divide(value)
