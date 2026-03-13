# Placeholder session module for future database integration.
from app.core.config import settings

def get_database_url() -> str:
    return settings.DATABASE_URL
