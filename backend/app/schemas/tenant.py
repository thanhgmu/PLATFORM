from pydantic import BaseModel

class TenantCreate(BaseModel):
    name: str

class TenantOut(BaseModel):
    id: int
    name: str
