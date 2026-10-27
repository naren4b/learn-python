# Lesson 19 — DIY: sys, argparse and os

Practice in your existing `lab/app.py` using `bash diy.sh`.

## Your Exercise

1. Import `sys` and display `sys.argv[0]` and `sys.argv[1:]`.
2. Switch to `argparse` with a positional `service` and optional `--port` (integer, default `8080`). Test `--help`.
3. Read `APP_PORT` using `os.getenv("APP_PORT", "8080")`. Convert to `int` if needed.
4. Compare CLI arguments with environment variables; they are separate inputs.

Try `APP_PORT=9090 python lab/app.py api` after adding the environment-variable example.

## Supplement: interactive input and multiple values

1. Prompt for a number using `input()` and convert it with `int()` inside a `try/except ValueError` loop.
2. Guard `sys.argv[1]` with `len(sys.argv) > 1` before accessing it.
3. Try `parser.add_argument("--service", action="append")` with repeated `--service` flags, and `nargs="+"` for multiple positional values.
4. Test age `0` with `if args.age is not None` rather than `if args.age`.
