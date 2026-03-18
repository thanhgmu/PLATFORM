from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, JSON

from app.db.base import Base


class ExecutionAudit(Base):
    __tablename__ = "execution_audits"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=True, index=True)
    orchestration_run_id = Column(Integer, ForeignKey("orchestration_runs.id"), nullable=True, index=True)
    agent_run_id = Column(Integer, ForeignKey("agent_runs.id"), nullable=True, index=True)
    event_type = Column(String, nullable=False, index=True)
    actor_type = Column(String, nullable=False, default="system")
    actor_id = Column(Integer, nullable=True)
    resource_type = Column(String, nullable=True)
    resource_id = Column(String, nullable=True)
    event_json = Column(JSON, nullable=True)
    occurred_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
