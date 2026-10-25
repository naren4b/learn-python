# Lesson 20 — DIY

Use your `lab/app.py`.

## Your Exercise

1. Run `docker ps --format '{{json .}}'` with `subprocess.run()`.
2. Capture stdout with `capture_output=True`, `text=True` and `check=True`.
3. Convert each nonempty stdout line into a dictionary with `json.loads()`.
4. Print each container's name and status.
5. Handle the case where no containers are running, and catch `FileNotFoundError` or `subprocess.CalledProcessError` if Docker is unavailable.

If you use Podman, substitute `podman` for `docker` and check the output structure.
