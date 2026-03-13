from fastapi import APIRouter
from app.services.plugin_loader import scan_plugins

router = APIRouter()

@router.get("/")
def list_plugins():
    return scan_plugins()

@router.post("/rescan")
def rescan_plugins():
    return {"discovered": [p["slug"] for p in scan_plugins()]}

@router.post("/{slug}/approve")
def approve_plugin(slug: str):
    return {"slug": slug, "approved": True}

@router.post("/{slug}/install")
def install_plugin(slug: str):
    return {"slug": slug, "installed": True}
