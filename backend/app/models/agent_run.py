from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, JSON, Text

from app.db.base import Base


class AgentRun(Base):
    __tablename__ = "agent_runs"

    id = Column(Integer, primary_key=True, index=True)
    orchestration_run_id = Column(Integer, ForeignKey("orchestration_runs.id"), nullable=False, index=True)
    #tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False, index=True)
    tenant_id = Column(Integer, nullable=False, index=True)
    agent_key = Column(String, nullable=False, index=True)
    step_no = Column(Integer, nullable=False)
    status = Column(String, nullable=False, default="queued")
    input_json = Column(JSON, nullable=True)
    output_json = Column(JSON, nullable=True)
    error_text = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    finished_at = Column(DateTime(timezone=True), nullable=True)
