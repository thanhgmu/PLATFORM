from sqlalchemy import Column, Integer, String
from app.db.base import Base

class InterestEvent(Base):
    __tablename__ = "interest_events"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    event_type = Column(String, nullable=False)
    channel = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    content = Column(String, nullable=False)
    timestamp = Column(String, nullable=False)
