from typing import Any, Dict, Optional
from sqlalchemy.orm import Session

from app.models.execution_audit import ExecutionAudit


class ExecutionAuditService:
    def record_event(
        self,
        db: Session,
        tenant_id: int,
        event_type: str,
        event_json: Optional[Dict[str, Any]] = None,
        case_id: Optional[int] = None,
        orchestration_run_id: Optional[int] = None,
        agent_run_id: Optional[int] = None,
        actor_type: str = "system",
        actor_id: Optional[int] = None,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
    ) -> ExecutionAudit:
        item = ExecutionAudit(
            tenant_id=tenant_id,
            case_id=case_id,
            orchestration_run_id=orchestration_run_id,
            agent_run_id=agent_run_id,
            event_type=event_type,
            actor_type=actor_type,
            actor_id=actor_id,
            resource_type=resource_type,
            resource_id=resource_id,
            event_json=event_json,
        )
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    def list_events(self, db: Session, tenant_id: Optional[int] = None, case_id: Optional[int] = None):
        query = db.query(ExecutionAudit)
        if tenant_id is not None:
            query = query.filter(ExecutionAudit.tenant_id == tenant_id)
        if case_id is not None:
            query = query.filter(ExecutionAudit.case_id == case_id)
        return query.order_by(ExecutionAudit.id.desc()).all()
