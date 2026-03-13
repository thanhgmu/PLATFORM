from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import require_permission
from app.db.session import get_db
from app.models.plugin import Plugin
from app.models.user import User

router = APIRouter()

@router.get("/plugins")
def marketplace_plugins(
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("marketplace:read")),
):
    plugins = db.query(Plugin).filter(Plugin.approved == True).all()
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
