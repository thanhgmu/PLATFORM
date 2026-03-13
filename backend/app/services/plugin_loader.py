import json
from pathlib import Path
from sqlalchemy.orm import Session
from app.models.plugin import Plugin

def scan_plugins():
    repo_root = Path(__file__).resolve().parents[3]
    plugins_dir = repo_root / "plugins"
    discovered = []

    if not plugins_dir.exists():
        return discovered

    for manifest_path in plugins_dir.glob("*/manifest.json"):
        try:
            data = json.loads(manifest_path.read_text(encoding="utf-8"))
            discovered.append({
                "slug": manifest_path.parent.name,
                "name": data.get("name", manifest_path.parent.name),
                "version": data.get("version", "0.0.0"),
            })
        except Exception:
            continue

    return discovered

def sync_plugins_to_db(db: Session, discovered: list[dict]):
    for item in discovered:
        existing = db.query(Plugin).filter(Plugin.slug == item["slug"]).first()
        if existing:
            existing.name = item["name"]
            existing.version = item["version"]
        else:
            db.add(Plugin(slug=item["slug"], name=item["name"], version=item["version"]))
    db.commit()
