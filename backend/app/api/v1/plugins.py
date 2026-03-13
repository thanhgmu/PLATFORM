from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, require_permission
from app.db.session import get_db
from app.models.plugin import Plugin
from app.models.user import User
from app.services.audit_log_service import record_audit
from app.services.plugin_loader import scan_plugins, sync_plugins_to_db

router = APIRouter()

@router.get("/")
def list_plugins(
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("plugin:read")),
):
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
def rescan_plugins(
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("plugin:manage")),
):
    discovered = scan_plugins()
    sync_plugins_to_db(db, discovered)
    record_audit(db, user.email, "plugin_rescan", None, "plugin_registry", None)
    return {"discovered": [p["slug"] for p in discovered]}

@router.post("/{slug}/approve")
def approve_plugin(
    slug: str,
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("plugin:approve")),
):
    plugin = db.query(Plugin).filter(Plugin.slug == slug).first()
    if not plugin:
        raise HTTPException(status_code=404, detail="Plugin not found")
    plugin.approved = True
    db.commit()
    record_audit(db, user.email, "plugin_approve", None, "plugin", slug)
    return {"slug": slug, "approved": True}

@router.post("/{slug}/install")
def install_plugin(
    slug: str,
    db: Session = Depends(get_db),
    user: User = Depends(require_permission("plugin:install")),
):
    plugin = db.query(Plugin).filter(Plugin.slug == slug).first()
    if not plugin:
        raise HTTPException(status_code=404, detail="Plugin not found")
    if not plugin.approved:
        raise HTTPException(status_code=400, detail="Plugin must be approved before install")
    plugin.installed = True
    db.commit()
    record_audit(db, user.email, "plugin_install", None, "plugin", slug)
    return {"slug": slug, "installed": True}
