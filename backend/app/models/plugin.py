from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class Plugin(Base):
    __tablename__ = "plugins"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    approved = Column(Boolean, default=False)
    installed = Column(Boolean, default=False)
