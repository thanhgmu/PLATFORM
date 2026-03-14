#!/bin/sh
set -e

echo "== root =="
curl -fsS http://localhost/ || exit 1

echo "== health =="
curl -fsS http://localhost/health || exit 1

echo "== backend docs =="
curl -fsS http://localhost:8000/docs > /dev/null || exit 1

echo "Smoke test passed."
