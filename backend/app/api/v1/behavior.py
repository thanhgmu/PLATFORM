from fastapi import APIRouter
from app.schemas.behavior import BehaviorEventIn
from app.services.behavior.ingestion_service import ingest_behavior_event
from app.services.behavior.recommendation_service import get_recommendation

router = APIRouter()

@router.post("/events")
def ingest_event(payload: BehaviorEventIn):
    return ingest_behavior_event(payload.model_dump())

@router.get("/recommendations/{user_id}")
def recommendation(user_id: int):
    return get_recommendation(user_id)
