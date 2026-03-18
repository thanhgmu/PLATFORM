from typing import Optional
from sqlalchemy.orm import Session

from app.models.agent_run import AgentRun
from app.models.orchestration_run import OrchestrationRun
from app.schemas.orchestration import OrchestrationRunCreate
from app.services.audit.execution_audit_service import ExecutionAuditService
from app.services.orchestration.dispatcher_service import DispatcherService
from app.services.orchestration.planner_service import PlannerService


class OrchestrationEngine:
    def __init__(self):
        self.planner = PlannerService()
        self.dispatcher = DispatcherService()
        self.audit = ExecutionAuditService()

    def create_run(self, db: Session, payload: OrchestrationRunCreate) -> OrchestrationRun:
        plan = self.planner.build_plan(payload.objective, payload.plan_json)
        item = OrchestrationRun(
            tenant_id=payload.tenant_id,
            case_id=payload.case_id,
            objective=payload.objective,
            status="planned",
            plan_json=plan,
        )
        db.add(item)
        db.commit()
        db.refresh(item)

        first_step = (plan.get("steps") or [{}])[0]
        agent_key = first_step.get("agent", "core.orchestrator")
        dispatch_result = self.dispatcher.dispatch(agent_key, {"objective": payload.objective, "case_id": payload.case_id})

        agent_run = AgentRun(
            orchestration_run_id=item.id,
            tenant_id=payload.tenant_id,
            agent_key=agent_key,
            step_no=1,
            status="completed",
            input_json={"objective": payload.objective, "case_id": payload.case_id},
            output_json=dispatch_result,
        )
        db.add(agent_run)
        db.commit()
        db.refresh(agent_run)

        self.audit.record_event(
            db=db,
            tenant_id=payload.tenant_id,
            case_id=payload.case_id,
            orchestration_run_id=item.id,
            agent_run_id=agent_run.id,
            event_type="orchestration_run_created",
            event_json={"plan": plan, "dispatch_result": dispatch_result},
        )
        return item

    def get_run(self, db: Session, run_id: int) -> Optional[OrchestrationRun]:
        return db.query(OrchestrationRun).filter(OrchestrationRun.id == run_id).first()

    def cancel_run(self, db: Session, run_id: int) -> Optional[OrchestrationRun]:
        item = self.get_run(db, run_id)
        if not item:
            return None
        item.status = "cancelled"
        db.commit()
        db.refresh(item)
        return item
