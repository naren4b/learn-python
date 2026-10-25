# Lesson 20 — Run Bash commands and inspect Docker containers

## Goal

Run a real command from Python, capture its output, and inspect structured results.

This lesson uses **`docker ps`** rather than `systemctl status docker`: Docker supports machine-readable output, while the default `systemctl status` text is intended for people.

## Bash command

```bash
docker ps --format '{{json .}}'
```

Docker prints **one JSON object per running container** (JSON Lines), not one JSON array. With no running containers, output is empty.

## Python example

```python
import json
import subprocess

result = subprocess.run(
    ["docker", "ps", "--format", "{{json .}}"],
    capture_output=True,
    text=True,
    check=True,
    timeout=10,
)

containers = [json.loads(line) for line in result.stdout.splitlines()]
print("Running containers:", len(containers))
for container in containers:
    print(container.get("Names"), container.get("Status"))
```

Each line becomes a Python **dictionary**, and `containers` is a **list of dictionaries**.

## Important details

- `subprocess.run()` runs Docker directly; a separate Bash script is optional.
- `capture_output=True` collects stdout and stderr separately.
- `check=True` raises `CalledProcessError` if Docker exits unsuccessfully.
- `json.loads(line)` parses one JSON object; `json.loads(result.stdout)` would fail when multiple JSON lines are present.
- `docker ps` shows running containers; `docker ps -a` includes stopped containers.
- On machines without Docker or daemon access, the command fails. On Podman-based WSL, use the equivalent `podman ps --format '{{json .}}'` but note output formats can differ.
- Do not infer container health from `Status` alone; Docker health-check state is separate.

[DIY](diy.md) · [Python reference](20_os_subprocess.py) · [Bash reference](status.sh) · [Python subprocess docs](https://docs.python.org/3.12/library/subprocess.html) · [Docker ps docs](https://docs.docker.com/reference/cli/docker/container/ls/)
