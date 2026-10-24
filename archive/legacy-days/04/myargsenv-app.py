# read the argumnents and environment variables
import os
import sys


def parse_arguments():
    """Parse command-line arguments and environment variables."""
    parsed_args = {}
    for arg in sys.argv[1:]:
        if arg.startswith("--"):
            arg = arg[2:]  # Remove leading '--'
            key, value = arg.split("=", 1)
            parsed_args[key] = value
        else:
            parsed_args[arg] = True  # Flag argument
    return parsed_args


if __name__ == "__main__":
    print("Script name:", sys.argv[0])
    print("Arguments:", sys.argv[1:])
    print("Environment variable MY_ENV_VAR:", os.getenv("MY_ENV_VAR", "Not Set"))

    args = parse_arguments()
    print("Parsed Arguments:", args)
