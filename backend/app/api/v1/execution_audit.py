from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.execution_audit import ExecutionAuditRead
from app.services.audit.execution_audit_service import ExecutionAuditService

router = APIRouter(prefix="/approvals", tags=["approvals"])
service = ExecutionAuditService()


@router.get("", response_model=list[ExecutionAuditRead])
def list_events(tenant_id: int | None = None, case_id: int | None = None, db: Session = Depends(get_db)):
    return service.list_events(db, tenant_id=tenant_id, case_id=case_id)
