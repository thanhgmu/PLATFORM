from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.behavior import BehaviorEventIn
from app.services.behavior.ingestion_service import ingest_behavior_event
from app.services.behavior.recommendation_service import get_recommendation

router = APIRouter()

@router.post("/events")
def ingest_event(
    payload: BehaviorEventIn,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ingest_behavior_event(db, payload.model_dump())

@router.get("/recommendations/{user_id}")
def recommendation(user_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_recommendation(db, user_id)
