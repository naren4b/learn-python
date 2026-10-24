# Lesson 12: Exception handling

## Objective
Handle expected failures without hiding unexpected bugs.

## Concepts
- `try` contains operations that might fail.
- `except ValueError` catches a specific invalid-value error.
- `except ZeroDivisionError` catches division by zero.
- `else` runs only if `try` finishes without an exception.
- `finally` runs whether or not an exception occurs.
- `raise` reports an error to the caller.

## Reference
Run `python lesson-12-except/12_exceptions.py`.

```text
Result: 5.0
Cleanup complete
Invalid number: abc
Cleanup complete
Cannot divide by zero
Cleanup complete
Raised: Value must be positive
Type: ValueError
Arguments: ('Value must be positive',)
Generic handler: ValueError: invalid literal for int() with base 10: 'not-a-number'
Traceback includes ZeroDivisionError: True
Re-raised: Original failure
```

## More exception examples

- `raise ValueError("Value must be positive")` creates and throws an error explicitly.
- `except ValueError as error:` gives access to the exception object: `str(error)`, `type(error).__name__`, and `error.args`.
- `except Exception as error:` catches most ordinary application exceptions. A bare `except:` is valid but also intercepts `KeyboardInterrupt` and `SystemExit`, so avoid it unless deliberately needed.
- `traceback.format_exc()` returns the current error's stack trace as text; `traceback.print_exc()` prints it.
- Plain `raise` inside an `except` block re-raises the active exception with its traceback. Outside an active exception handler, plain `raise` is invalid at runtime.

## Important lines explained
- `int(raw)`: Converts text to an integer; invalid input raises `ValueError`.
- `except ValueError:`: Handles only the expected conversion error rather than catching every failure.
- `finally:`: Runs cleanup code even if the operation fails.

**Trade-off:** Catch specific exceptions, and avoid silent `except: pass` blocks that hide defects.

See [DIY](diy.md) and [reference implementation](12_exceptions.py). No extra packages.
