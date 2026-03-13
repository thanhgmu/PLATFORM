from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.plugin import Plugin
from app.models.user import User

router = APIRouter()

@router.get("/plugins")
def marketplace_plugins(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    plugins = db.query(Plugin).all()
    return [
        {
            "slug": p.slug,
            "name": p.name,
            "version": p.version,
            "approved": p.approved,
            "installed": p.installed,
        }
        for p in plugins
    ]
