from sqlalchemy import Column, Integer, String
from app.db.base import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    actor = Column(String, nullable=False)
    action = Column(String, nullable=False)
    tenant_id = Column(Integer, nullable=True)
    resource_type = Column(String, nullable=False)
    resource_id = Column(String, nullable=True)
    timestamp = Column(String, nullable=False)
