# Lesson 20 — DIY: Bash output into a Python dict

Use your existing `lab/app.py`.

## Your Exercise

1. Create `lab/status.sh` that prints one JSON object containing a service name, status and port.
2. In `lab/app.py`, run the script using `subprocess.run(["bash", "lab/status.sh"], capture_output=True, text=True, check=True)`.
3. Convert `result.stdout` into a dictionary using `json.loads()`.
4. Print the service name and status from the dictionary.
5. Optional: test what happens when the script prints invalid JSON.

**Reminder:** Bash stdout should contain only JSON; write logs and errors to stderr.
