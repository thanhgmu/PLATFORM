from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.audit_log import AuditLog

def record_audit(
    db: Session,
    actor: str,
    action: str,
    tenant_id: int | None,
    resource_type: str,
    resource_id: str | None,
) -> AuditLog:
    row = AuditLog(
        actor=actor,
        action=action,
        tenant_id=tenant_id,
        resource_type=resource_type,
        resource_id=resource_id,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row
