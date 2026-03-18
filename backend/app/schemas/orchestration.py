from typing import Any, Dict, Optional
from pydantic import BaseModel


class OrchestrationRunCreate(BaseModel):
    tenant_id: int
    case_id: int
    objective: str
    plan_json: Optional[Dict[str, Any]] = None


class OrchestrationRunRead(BaseModel):
    id: int
    tenant_id: int
    case_id: int
    objective: str
    status: str
    plan_json: Optional[Dict[str, Any]] = None

    class Config:
        orm_mode = True
