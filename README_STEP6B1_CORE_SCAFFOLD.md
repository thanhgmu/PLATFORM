# Step 6B1 — Core Scaffold

## Goal
Realign the repo so the Platform Core reflects the new architecture without breaking the current skeleton.

## Added domains
- Case Management
- Agent Registry
- Orchestration Engine
- Shared Context
- Approval Workflow
- Execution Audit

## Files added
- `backend/app/models/case.py`
- `backend/app/models/case_message.py`
- `backend/app/models/agent_definition.py`
- `backend/app/models/orchestration_run.py`
- `backend/app/models/agent_run.py`
- `backend/app/models/approval_request.py`
- `backend/app/models/shared_context_entry.py`
- `backend/app/models/execution_audit.py`
- matching files under `schemas/`, `services/`, and `api/v1/`

## Safe boundary rules
- OpenClaw remains behind adapter/service boundaries.
- Business plugins remain outside backend core.
- Every new domain object is tenant-scoped.
