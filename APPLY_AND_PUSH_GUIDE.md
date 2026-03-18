# PLATFORM Step 6B Pack — Apply and Push Guide

This pack is designed to be overlaid onto your existing `PLATFORM` local repository.
It adds the Step 6B architecture scaffolding for:
- Case Management
- Agent Registry
- Orchestration Engine
- Shared Context
- Approval Workflow
- Execution Audit

## 1) Prepare local repo

```bash
cd /path/to/PLATFORM
cp .env.example .env
```

## 2) Copy this pack into the repo

Option A — manual copy:
- unzip this pack
- copy the contained files into the matching paths in your local repo

Option B — use helper script:

```bash
bash COPY_INTO_REPO.sh /path/to/PLATFORM
```

## 3) Review before commit

```bash
cd /path/to/PLATFORM
git status
git diff --stat
git diff
```

## 4) Commit in safe batches

```bash
git checkout -b step6b-architecture-realignment

git add backend/app/models backend/app/schemas backend/app/services backend/app/api/v1 backend/app/db/base.py backend/app/main.py

git commit -m "Step 6B1 add case, orchestration, approval and shared context scaffolding"

git add .env.example docker-compose.yml README_DEPLOY_VPS.md backend/app/core/config.py plugins/bctc-tax-ai/manifest.json

git commit -m "Step 6B2 align runtime and plugin manifest for updated platform core"

git add README_STEP6B1_CORE_SCAFFOLD.md README_STEP6B2_DB_READY.md README_STEP6B3_ORCHESTRATION.md README_STEP6B4_VPS_READY.md

git commit -m "Step 6B3 add architecture and deployment step docs"
```

## 5) Push to GitHub

```bash
git push -u origin step6b-architecture-realignment
```

If you want to update `main` directly after review:

```bash
git checkout main
git pull origin main
git merge --ff-only step6b-architecture-realignment
git push origin main
```

## 6) Smoke check locally before PLATFORM 06

```bash
docker compose up -d --build
curl http://127.0.0.1/health
curl http://127.0.0.1/ready
curl http://127.0.0.1:8000/api/v1/agents
curl http://127.0.0.1:8000/api/v1/cases
```

## Notes

- This pack is intentionally additive-first.
- It does not move OpenClaw into core.
- It keeps plugin logic outside the backend core.
- It keeps startup compatible with the current repo pattern by continuing to rely on `Base.metadata.create_all()`.
- In a later hardening phase, you should replace create-all with full Alembic migrations.
