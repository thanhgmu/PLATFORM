from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session

from app.models.approval_request import ApprovalRequest
from app.schemas.approvals import ApprovalRequestCreate


class ApprovalService:
    def create_request(self, db: Session, payload: ApprovalRequestCreate) -> ApprovalRequest:
        item = ApprovalRequest(
            tenant_id=payload.tenant_id,
            case_id=payload.case_id,
            orchestration_run_id=payload.orchestration_run_id,
            action_type=payload.action_type,
            payload_json=payload.payload_json,
            requested_by=payload.requested_by,
            status="pending",
        )
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    def list_requests(self, db: Session, tenant_id: Optional[int] = None):
        query = db.query(ApprovalRequest)
        if tenant_id is not None:
            query = query.filter(ApprovalRequest.tenant_id == tenant_id)
        return query.order_by(ApprovalRequest.id.desc()).all()

    def approve(self, db: Session, approval_id: int, decided_by: Optional[int] = None) -> Optional[ApprovalRequest]:
        item = db.query(ApprovalRequest).filter(ApprovalRequest.id == approval_id).first()
        if not item:
            return None
        item.status = "approved"
        item.approved_by = decided_by
        item.decided_at = datetime.utcnow()
        db.commit()
        db.refresh(item)
        return item

    def reject(self, db: Session, approval_id: int, decided_by: Optional[int] = None) -> Optional[ApprovalRequest]:
        item = db.query(ApprovalRequest).filter(ApprovalRequest.id == approval_id).first()
        if not item:
            return None
        item.status = "rejected"
        item.approved_by = decided_by
        item.decided_at = datetime.utcnow()
        db.commit()
        db.refresh(item)
        return item
