from fastapi import APIRouter
from app.schemas.openclaw import OpenClawEventIn, OpenClawMessageIn
from app.services.adapters.openclaw_adapter import OpenClawAdapter

router = APIRouter()
adapter = OpenClawAdapter()

@router.post("/events")
def ingest_event(payload: OpenClawEventIn):
    return adapter.ingest_event(payload.model_dump())

@router.post("/send-message")
def send_message(payload: OpenClawMessageIn):
    return adapter.send_message(payload.model_dump())

@router.post("/context")
def get_context(payload: dict):
    return adapter.get_context(payload)
