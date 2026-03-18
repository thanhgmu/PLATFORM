from typing import Dict, Any


class PlannerService:
    def build_plan(self, objective: str, existing_plan: Dict[str, Any] | None = None) -> Dict[str, Any]:
        if existing_plan:
            return existing_plan
        return {
            "objective": objective,
            "steps": [
                {"step": 1, "agent": "core.case_manager", "action": "triage_case"},
                {"step": 2, "agent": "core.orchestrator", "action": "plan_next_actions"},
            ],
        }
