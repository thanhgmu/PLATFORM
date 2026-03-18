from typing import Optional
from sqlalchemy.orm import Session

from app.models.case import Case
from app.models.case_message import CaseMessage
from app.schemas.cases import CaseCreate, CaseMessageCreate


class CaseService:
    def create_case(self, db: Session, payload: CaseCreate) -> Case:
        item = Case(
            tenant_id=payload.tenant_id,
            title=payload.title,
            created_by=payload.created_by,
            assigned_to=payload.assigned_to,
            status="open",
        )
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    def list_cases(self, db: Session, tenant_id: Optional[int] = None, status: Optional[str] = None):
        query = db.query(Case)
        if tenant_id is not None:
            query = query.filter(Case.tenant_id == tenant_id)
        if status:
            query = query.filter(Case.status == status)
        return query.order_by(Case.id.desc()).all()

    def get_case(self, db: Session, case_id: int) -> Optional[Case]:
        return db.query(Case).filter(Case.id == case_id).first()

    def add_message(self, db: Session, case_id: int, payload: CaseMessageCreate) -> CaseMessage:
        item = CaseMessage(
            case_id=case_id,
            tenant_id=payload.tenant_id,
            role=payload.role,
            author_type=payload.author_type,
            author_id=payload.author_id,
            content=payload.content,
            metadata_json=payload.metadata_json,
        )
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
