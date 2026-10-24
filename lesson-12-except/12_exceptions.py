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


# Example: raise explicitly and inspect the caught exception object.
def require_positive(value: int) -> int:
    if value <= 0:
        raise ValueError("Value must be positive")
    return value


try:
    require_positive(-1)
except ValueError as error:
    print(f"Raised: {error}")
    print(f"Type: {type(error).__name__}")
    print(f"Arguments: {error.args}")


# Example: catch general application errors (not a bare except).
try:
    int("not-a-number")
except Exception as error:
    print(f"Generic handler: {type(error).__name__}: {error}")


# Example: render a traceback as text; print_exc() writes to stderr.
import traceback

try:
    1 / 0
except ZeroDivisionError:
    trace = traceback.format_exc()
    print(f"Traceback includes ZeroDivisionError: {'ZeroDivisionError' in trace}")


# Example: re-raise an active exception for the caller to handle.
def rethrow_error() -> None:
    try:
        raise RuntimeError("Original failure")
    except RuntimeError:
        raise  # Preserve the active exception and traceback.


try:
    rethrow_error()
except RuntimeError as error:
    print(f"Re-raised: {error}")
