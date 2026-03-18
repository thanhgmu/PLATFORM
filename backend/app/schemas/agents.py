from typing import List, Optional
from pydantic import BaseModel


class AgentDefinitionRead(BaseModel):
    id: int
    tenant_id: Optional[int] = None
    key: str
    display_name: str
    source_type: str
    adapter_name: Optional[str] = None
    capabilities_json: Optional[List[str]] = None
    enabled: bool

    class Config:
        orm_mode = True


class AgentDefinitionUpdate(BaseModel):
    enabled: bool
