from fastapi import APIRouter
from app.schemas.consent import ConsentCreate

router = APIRouter()

_CONSENTS: list[dict] = []

@router.post("/")
def create_consent(payload: ConsentCreate):
    data = payload.model_dump()
    _CONSENTS.append(data)
    return data

@router.get("/")
def list_consents():
    return _CONSENTS
