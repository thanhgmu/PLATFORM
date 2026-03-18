from typing import Any, Dict, Optional
from pydantic import BaseModel


class SharedContextEntryCreate(BaseModel):
    tenant_id: int
    case_id: Optional[int] = None
    scope_type: str = "case"
    scope_key: Optional[str] = None
    content_type: str = "text"
    content: Optional[str] = None
    storage_ref: Optional[str] = None
    vector_ref: Optional[str] = None
    metadata_json: Optional[Dict[str, Any]] = None


class SharedContextEntryRead(BaseModel):
    id: int
    tenant_id: int
    case_id: Optional[int] = None
    scope_type: str
    scope_key: Optional[str] = None
    content_type: str
    content: Optional[str] = None
    storage_ref: Optional[str] = None
    vector_ref: Optional[str] = None
    metadata_json: Optional[Dict[str, Any]] = None

    class Config:
        orm_mode = True
