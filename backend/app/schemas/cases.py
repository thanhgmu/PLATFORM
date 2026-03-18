from typing import Any, Dict, Optional
from pydantic import BaseModel


class CaseCreate(BaseModel):
    tenant_id: int
    title: str
    created_by: Optional[int] = None
    assigned_to: Optional[int] = None


class CaseRead(BaseModel):
    id: int
    tenant_id: int
    title: str
    status: str
    created_by: Optional[int] = None
    assigned_to: Optional[int] = None

    class Config:
        orm_mode = True


class CaseMessageCreate(BaseModel):
    tenant_id: int
    role: str = "user"
    author_type: str = "user"
    author_id: Optional[int] = None
    content: str
    metadata_json: Optional[Dict[str, Any]] = None


class CaseMessageRead(BaseModel):
    id: int
    case_id: int
    tenant_id: int
    role: str
    author_type: str
    author_id: Optional[int] = None
    content: str
    metadata_json: Optional[Dict[str, Any]] = None

    class Config:
        orm_mode = True
