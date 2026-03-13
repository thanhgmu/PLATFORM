from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.plugin import Plugin
from app.models.user import User
from app.services.plugin_loader import scan_plugins, sync_plugins_to_db

router = APIRouter()

@router.get("/")
def list_plugins(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
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

@router.post("/rescan")
def rescan_plugins(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    discovered = scan_plugins()
    sync_plugins_to_db(db, discovered)
    return {"discovered": [p["slug"] for p in discovered]}

@router.post("/{slug}/approve")
def approve_plugin(slug: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    plugin = db.query(Plugin).filter(Plugin.slug == slug).first()
    if not plugin:
        return {"error": "plugin not found"}
    plugin.approved = True
    db.commit()
    return {"slug": slug, "approved": True}

@router.post("/{slug}/install")
def install_plugin(slug: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    plugin = db.query(Plugin).filter(Plugin.slug == slug).first()
    if not plugin:
        return {"error": "plugin not found"}
    plugin.installed = True
    db.commit()
    return {"slug": slug, "installed": True}
