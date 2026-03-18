from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.approvals import ApprovalRequestCreate, ApprovalRequestRead, ApprovalDecision
from app.services.approvals.approval_service import ApprovalService

router = APIRouter()
service = ApprovalService()


@router.post("", response_model=ApprovalRequestRead)
def create_request(payload: ApprovalRequestCreate, db: Session = Depends(get_db)):
    return service.create_request(db, payload)


@router.get("", response_model=list[ApprovalRequestRead])
def list_requests(tenant_id: int | None = None, db: Session = Depends(get_db)):
    return service.list_requests(db, tenant_id=tenant_id)


@router.post("/{approval_id}/approve", response_model=ApprovalRequestRead)
def approve_request(approval_id: int, payload: ApprovalDecision, db: Session = Depends(get_db)):
    item = service.approve(db, approval_id=approval_id, decided_by=payload.decided_by)
    if not item:
        raise HTTPException(status_code=404, detail="Approval request not found")
    return item


@router.post("/{approval_id}/reject", response_model=ApprovalRequestRead)
def reject_request(approval_id: int, payload: ApprovalDecision, db: Session = Depends(get_db)):
    item = service.reject(db, approval_id=approval_id, decided_by=payload.decided_by)
    if not item:
        raise HTTPException(status_code=404, detail="Approval request not found")
    return item
