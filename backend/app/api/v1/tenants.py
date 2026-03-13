from fastapi import APIRouter
from app.schemas.tenant import TenantCreate

router = APIRouter()

@router.post("/")
def create_tenant(payload: TenantCreate):
    return {"id": 1, "name": payload.name}

@router.get("/")
def list_tenants():
    return [{"id": 1, "name": "Default Tenant"}]
