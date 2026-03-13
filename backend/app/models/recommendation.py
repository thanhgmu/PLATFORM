from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    preferred_channels = Column(String, nullable=False, default="[]")
    next_best_action = Column(String, nullable=False, default="send_contextual_followup")
    topic_tags = Column(String, nullable=False, default="[]")
