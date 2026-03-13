from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Consent(Base):
    __tablename__ = "consents"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    scope = Column(String, nullable=False)
    status = Column(String, nullable=False, default="granted")
    retention_days = Column(Integer, nullable=False, default=30)
