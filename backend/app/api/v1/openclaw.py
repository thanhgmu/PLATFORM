from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, require_permission
from app.db.session import get_db
from app.models.user import User
from app.schemas.openclaw import OpenClawEventIn, OpenClawMessageIn
from app.services.adapters.openclaw_adapter import OpenClawAdapter
from app.services.audit_log_service import record_audit

router = APIRouter()
adapter = OpenClawAdapter()

@router.post("/events")
def ingest_event(
    payload: OpenClawEventIn,
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("openclaw:ingest")),
):
    result = adapter.ingest_event(payload.model_dump())
    record_audit(db, user.email, "openclaw_ingest_event", payload.tenant_id, "openclaw_event", payload.event_type)
    return result

@router.post("/send-message")
def send_message(
    payload: OpenClawMessageIn,
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("openclaw:send")),
):
    result = adapter.send_message(payload.model_dump())
    record_audit(db, user.email, "openclaw_send_message", payload.tenant_id, "openclaw_message", payload.channel)
    return result

@router.post("/context")
def get_context(
    payload: dict,
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("openclaw:context")),
):
    result = adapter.get_context(payload)
    record_audit(db, user.email, "openclaw_get_context", payload.get("tenant_id"), "openclaw_context", str(payload.get("user_id")))
    return result
