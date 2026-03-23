from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.cases import CaseCreate, CaseRead, CaseMessageCreate, CaseMessageRead
from app.services.cases.case_service import CaseService

router = APIRouter(prefix="/cases", tags=["cases"])
service = CaseService()


@router.post("", response_model=CaseRead)
def create_case(payload: CaseCreate, db: Session = Depends(get_db)):
    return service.create_case(db, payload)


@router.get("", response_model=list[CaseRead])
def list_cases(tenant_id: int | None = None, status: str | None = None, db: Session = Depends(get_db)):
    return service.list_cases(db, tenant_id=tenant_id, status=status)


@router.get("/{case_id}", response_model=CaseRead)
def get_case(case_id: int, db: Session = Depends(get_db)):
    item = service.get_case(db, case_id)
    if not item:
        raise HTTPException(status_code=404, detail="Case not found")
    return item


@router.post("/{case_id}/messages", response_model=CaseMessageRead)
def add_case_message(case_id: int, payload: CaseMessageCreate, db: Session = Depends(get_db)):
    case_item = service.get_case(db, case_id)
    if not case_item:
        raise HTTPException(status_code=404, detail="Case not found")
    return service.add_message(db, case_id, payload)
