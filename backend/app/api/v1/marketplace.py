from fastapi import APIRouter
from app.services.plugin_loader import scan_plugins

router = APIRouter()

@router.get("/plugins")
def marketplace_plugins():
    return scan_plugins()
