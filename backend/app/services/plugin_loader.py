import json
from pathlib import Path

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
                "approved": False,
                "installed": False,
            })
        except Exception:
            continue

    return discovered
