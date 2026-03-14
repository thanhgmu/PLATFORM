# Step 6A Runtime & Deployment

This archive is focused on running the current Platform Core on a VPS with fewer surprises.

## What it adds
- stronger docker-compose with service health checks
- backend startup script
- database wait script
- admin bootstrap/seed script
- /health and /ready endpoints
- nginx health proxy
- VPS smoke test script
- richer .env.example

## How to use
1. Extract this ZIP into the root of your local `PLATFORM` repo.
2. Overwrite files if asked.
3. Commit and push:

   git add .
   git commit -m "Add Step 6A runtime and deployment hardening"
   git push origin main

## VPS run
   cp .env.example .env
   docker compose up -d --build

## Quick checks
   docker compose ps
   curl http://YOUR_SERVER_IP/health
   curl http://YOUR_SERVER_IP:8000/docs
