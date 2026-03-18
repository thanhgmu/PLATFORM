from typing import Optional
from sqlalchemy.orm import Session

from app.models.shared_context_entry import SharedContextEntry
from app.schemas.shared_context import SharedContextEntryCreate


class SharedContextService:
    def create_entry(self, db: Session, payload: SharedContextEntryCreate) -> SharedContextEntry:
        item = SharedContextEntry(
            tenant_id=payload.tenant_id,
            case_id=payload.case_id,
            scope_type=payload.scope_type,
            scope_key=payload.scope_key,
            content_type=payload.content_type,
            content=payload.content,
            storage_ref=payload.storage_ref,
            vector_ref=payload.vector_ref,
            metadata_json=payload.metadata_json,
        )
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    def list_entries(self, db: Session, tenant_id: int, case_id: Optional[int] = None):
        query = db.query(SharedContextEntry).filter(SharedContextEntry.tenant_id == tenant_id)
        if case_id is not None:
            query = query.filter(SharedContextEntry.case_id == case_id)
        return query.order_by(SharedContextEntry.id.desc()).all()
