from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey

from app.db.base import Base


class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    #tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False, index=True)
    tenant_id = Column(Integer, nullable=False, index=True)
    title = Column(String, nullable=False)
    status = Column(String, nullable=False, default="open", index=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
