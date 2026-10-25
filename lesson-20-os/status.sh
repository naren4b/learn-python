#!/usr/bin/env bash
set -euo pipefail

# Ask Docker to emit one JSON object per running container.
docker ps --format '{{json .}}'
