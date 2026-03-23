from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, JSON, Text

from app.db.base import Base


class CaseMessage(Base):
    __tablename__ = "case_messages"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=False, index=True)
    #tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False, index=True)
    tenant_id = Column(Integer, nullable=False, index=True)
    role = Column(String, nullable=False, default="user")
    author_type = Column(String, nullable=False, default="user")
    author_id = Column(Integer, nullable=True)
    content = Column(Text, nullable=False)
    metadata_json = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
