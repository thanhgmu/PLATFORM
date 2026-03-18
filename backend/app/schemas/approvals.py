from typing import Any, Dict, Optional
from pydantic import BaseModel


class ApprovalRequestCreate(BaseModel):
    tenant_id: int
    case_id: Optional[int] = None
    orchestration_run_id: Optional[int] = None
    action_type: str
    payload_json: Optional[Dict[str, Any]] = None
    requested_by: Optional[int] = None


class ApprovalRequestRead(BaseModel):
    id: int
    tenant_id: int
    case_id: Optional[int] = None
    orchestration_run_id: Optional[int] = None
    action_type: str
    payload_json: Optional[Dict[str, Any]] = None
    status: str
    requested_by: Optional[int] = None
    approved_by: Optional[int] = None

    class Config:
        orm_mode = True


class ApprovalDecision(BaseModel):
    decided_by: Optional[int] = None
