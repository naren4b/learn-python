# Load env variables
import os

my_passkey = os.getenv("PASSKEY")
if my_passkey:
    print(f"My passkey is: {my_passkey}")
else:
    print("No passkey found in environment variables.")
