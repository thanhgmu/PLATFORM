from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, JSON, Text

from app.db.base import Base


class OrchestrationRun(Base):
    __tablename__ = "orchestration_runs"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=False, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False, index=True)
    objective = Column(Text, nullable=False)
    status = Column(String, nullable=False, default="queued", index=True)
    plan_json = Column(JSON, nullable=True)
    started_at = Column(DateTime(timezone=True), nullable=True)
    finished_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
