# Day 2: Do it yourself

Use WSL. Keep using the same local scratch files:

```bash
mkdir -p /mnt/c/code/personal/learn-python/lab
cd /mnt/c/code/personal/learn-python/lab
touch app.py requirements.txt
vi app.py
python app.py
```

Write your own program that:
1. Stores a city as text, an age as a whole number, a price as a decimal number, and a ready flag as a boolean.
2. Prints each value and its type using `type(value).__name__`.
3. Prints the next year's age using `age + 1`.

Now change `age` from a number to the string `"45"`. Run it and observe what happens. Fix it using `int(age)`.

No packages to install. Do not commit your local `app.py`. Open [the reference solution](02_types.py) only if stuck.
