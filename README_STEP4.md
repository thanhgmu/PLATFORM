# Step 4 DB-backed foundation

This archive upgrades the backend foundation to use:
- SQLAlchemy models
- DB session
- JWT auth utilities
- DB-backed auth/tenant/plugins/consent/behavior
- Alembic skeleton
- updated Docker and docker-compose for PostgreSQL

## How to use
1. Extract this ZIP into the root of your local `PLATFORM` repo.
2. Overwrite files if asked.
3. Commit and push:

   git add .
   git commit -m "Add Step 4 DB-backed foundation"
   git push origin main
