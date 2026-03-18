# Step 6B2 — DB Ready

## Goal
Make the current repo deployable with the new architecture while still following the existing startup pattern.

## Current approach
- Keep `Base.metadata.create_all()` for compatibility with the current repo.
- Import the new models through `backend/app/db/base.py` so table creation sees them.

## Next hardening step
Move to proper Alembic migrations after the new domain has stabilized.
