from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.shared_context import SharedContextEntryCreate, SharedContextEntryRead
from app.services.context.shared_context_service import SharedContextService

router = APIRouter(prefix="/shared-context", tags=["shared_context"])
service = SharedContextService()


@router.post("", response_model=SharedContextEntryRead)
def create_entry(payload: SharedContextEntryCreate, db: Session = Depends(get_db)):
    return service.create_entry(db, payload)


@router.get("", response_model=list[SharedContextEntryRead])
def list_entries(tenant_id: int, case_id: int | None = None, db: Session = Depends(get_db)):
    return service.list_entries(db, tenant_id=tenant_id, case_id=case_id)
