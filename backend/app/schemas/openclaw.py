from pydantic import BaseModel

class OpenClawEventIn(BaseModel):
    tenant_id: int | None = None
    user_id: int | None = None
    channel: str
    event_type: str
    content_type: str
    content: str
    timestamp: str

class OpenClawMessageIn(BaseModel):
    tenant_id: int | None = None
    user_id: int | None = None
    channel: str
    message: str
