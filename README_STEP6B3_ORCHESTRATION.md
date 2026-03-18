# Step 6B3 — Orchestration Wiring

## Goal
Introduce an orchestration layer that can evolve into full multi-agent execution without forcing a worker split yet.

## Included services
- `case_service`
- `agent_registry_service`
- `orchestration_engine`
- `planner_service`
- `dispatcher_service`
- `approval_service`
- `shared_context_service`
- `execution_audit_service`

## Initial runtime behavior
- in-process orchestration
- approval-aware action flow
- shared context stored in DB metadata now, extensible later to blob/vector systems
