from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, JSON, Boolean

from app.db.base import Base


class AgentDefinition(Base):
    __tablename__ = "agent_definitions"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=True, index=True)
    key = Column(String, nullable=False, unique=True, index=True)
    display_name = Column(String, nullable=False)
    source_type = Column(String, nullable=False, default="core")
    adapter_name = Column(String, nullable=True)
    capabilities_json = Column(JSON, nullable=True)
    enabled = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
