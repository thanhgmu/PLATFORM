from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, JSON

from app.db.base import Base


class ApprovalRequest(Base):
    __tablename__ = "approval_requests"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=True, index=True)
    orchestration_run_id = Column(Integer, ForeignKey("orchestration_runs.id"), nullable=True, index=True)
    action_type = Column(String, nullable=False)
    payload_json = Column(JSON, nullable=True)
    status = Column(String, nullable=False, default="pending", index=True)
    requested_by = Column(Integer, nullable=True)
    approved_by = Column(Integer, nullable=True)
    decided_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
