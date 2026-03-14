#!/bin/sh
set -e

echo "[platform] waiting for database..."
python /app/scripts/wait_for_db.py

echo "[platform] bootstrapping database..."
python /app/scripts/bootstrap_db.py

echo "[platform] starting api..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
