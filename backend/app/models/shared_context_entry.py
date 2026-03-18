from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, JSON, Text

from app.db.base import Base


class SharedContextEntry(Base):
    __tablename__ = "shared_context_entries"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=True, index=True)
    scope_type = Column(String, nullable=False, default="case")
    scope_key = Column(String, nullable=True)
    content_type = Column(String, nullable=False, default="text")
    content = Column(Text, nullable=True)
    storage_ref = Column(String, nullable=True)
    vector_ref = Column(String, nullable=True)
    metadata_json = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
