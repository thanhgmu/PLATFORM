from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import require_permission
from app.db.session import get_db
from app.models.user import User
from app.schemas.behavior import BehaviorEventIn
from app.services.audit_log_service import record_audit
from app.services.behavior.ingestion_service import ingest_behavior_event
from app.services.behavior.recommendation_service import get_recommendation

router = APIRouter()

@router.post("/events")
def ingest_event(
    payload: BehaviorEventIn,
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("behavior:ingest")),
):
    result = ingest_behavior_event(db, payload.model_dump())
    record_audit(db, user.email, "behavior_ingest", payload.tenant_id, "behavior_event", str(result.get("id")))
    return result

@router.get("/recommendations/{user_id}")
def recommendation(
    user_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("behavior:read")),
):
    return get_recommendation(db, user_id)
