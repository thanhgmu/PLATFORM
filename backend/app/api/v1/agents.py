from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.agents import AgentDefinitionRead, AgentDefinitionUpdate
from app.services.registry.agent_registry_service import AgentRegistryService

router = APIRouter()
service = AgentRegistryService()


@router.get("", response_model=list[AgentDefinitionRead])
def list_agents(tenant_id: int | None = None, db: Session = Depends(get_db)):
    return service.list_agents(db, tenant_id=tenant_id)


@router.patch("/{agent_key}", response_model=AgentDefinitionRead)
def update_agent(agent_key: str, payload: AgentDefinitionUpdate, db: Session = Depends(get_db)):
    item = service.update_enabled(db, agent_key=agent_key, enabled=payload.enabled)
    if not item:
        raise HTTPException(status_code=404, detail="Agent not found")
    return item
