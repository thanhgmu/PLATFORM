from pydantic import BaseModel

class ConsentCreate(BaseModel):
    tenant_id: int | None = None
    user_id: int | None = None
    scope: str
    status: str = "granted"
    retention_days: int = 30
