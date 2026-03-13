from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, require_permission
from app.db.session import get_db
from app.models.consent import Consent
from app.models.user import User
from app.schemas.consent import ConsentCreate
from app.services.audit_log_service import record_audit

router = APIRouter()

@router.post("/")
def create_consent(
    payload: ConsentCreate,
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("consent:manage")),
):
    consent = Consent(**payload.model_dump())
    db.add(consent)
    db.commit()
    db.refresh(consent)
    record_audit(db, user.email, "consent_create", payload.tenant_id, "consent", str(consent.id))
    return payload.model_dump()

@router.get("/")
def list_consents(
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("consent:read")),
):
    consents = db.query(Consent).all()
    return [
        {
            "id": c.id,
            "tenant_id": c.tenant_id,
            "user_id": c.user_id,
            "scope": c.scope,
            "status": c.status,
            "retention_days": c.retention_days,
        }
        for c in consents
    ]
