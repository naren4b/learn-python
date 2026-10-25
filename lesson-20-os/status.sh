#!/usr/bin/env bash
set -euo pipefail
# Emit one valid JSON object to stdout for Python to parse.
printf '{"service":"api","status":"healthy","port":8080}\n'
