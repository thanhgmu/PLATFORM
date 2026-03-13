from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.tenant import Tenant
from app.models.user import User
from app.schemas.tenant import TenantCreate

router = APIRouter()

@router.post("/")
def create_tenant(
    payload: TenantCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    tenant = Tenant(name=payload.name, owner_user_id=user.id)
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    return {"id": tenant.id, "name": tenant.name}

@router.get("/")
def list_tenants(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    tenants = db.query(Tenant).all()
    return [{"id": t.id, "name": t.name} for t in tenants]
