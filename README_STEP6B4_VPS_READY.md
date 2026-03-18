# Step 6B4 — VPS Ready

## Goal
Prepare the repo so the next thread can focus on deployment rather than structural refactor.

## Runtime updates
- `docker-compose.yml` now uses `.env`
- named volumes added for persistence
- shared context and orchestration envs added
- deploy README expanded into a real checklist

## Before PLATFORM 06
1. push this Step 6B branch to GitHub
2. confirm `docker compose up -d --build` works locally
3. only then move to VPS deployment
