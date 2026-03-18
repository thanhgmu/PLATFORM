from typing import Any, Dict, Optional
from pydantic import BaseModel


class ExecutionAuditRead(BaseModel):
    id: int
    tenant_id: int
    case_id: Optional[int] = None
    orchestration_run_id: Optional[int] = None
    agent_run_id: Optional[int] = None
    event_type: str
    actor_type: str
    actor_id: Optional[int] = None
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    event_json: Optional[Dict[str, Any]] = None

    class Config:
        orm_mode = True
