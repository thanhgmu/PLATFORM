from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.agent_definition import AgentDefinition
from app.models.plugin import Plugin
from app.services.plugin_loader import scan_plugins


class AgentRegistryService:
    def ensure_seed_agents(self, db: Session) -> None:
        if db.query(AgentDefinition).count() > 0:
            return

        builtins = [
            {
                "key": "core.case_manager",
                "display_name": "Case Manager",
                "source_type": "core",
                "adapter_name": None,
                "capabilities_json": ["case_management", "routing"],
            },
            {
                "key": "core.orchestrator",
                "display_name": "Orchestrator",
                "source_type": "core",
                "adapter_name": None,
                "capabilities_json": ["planning", "dispatch", "approval_checks"],
            },
            {
                "key": "adapter.openclaw",
                "display_name": "OpenClaw Adapter",
                "source_type": "adapter",
                "adapter_name": "openclaw",
                "capabilities_json": ["external_agent_bridge"],
            },
        ]

        discovered_plugins = scan_plugins()
        for plugin in discovered_plugins:
            builtins.append(
                {
                    "key": f"plugin.{plugin['slug']}",
                    "display_name": plugin["name"],
                    "source_type": "plugin",
                    "adapter_name": plugin.get("adapter_binding"),
                    "capabilities_json": plugin.get("capabilities") or ["plugin_capability"],
                }
            )

        for item in builtins:
            db.add(
                AgentDefinition(
                    key=item["key"],
                    display_name=item["display_name"],
                    source_type=item["source_type"],
                    adapter_name=item.get("adapter_name"),
                    capabilities_json=item.get("capabilities_json"),
                    enabled=True,
                )
            )
        db.commit()

    def list_agents(self, db: Session, tenant_id: Optional[int] = None) -> List[AgentDefinition]:
        self.ensure_seed_agents(db)
        query = db.query(AgentDefinition)
        if tenant_id is not None:
            query = query.filter((AgentDefinition.tenant_id == tenant_id) | (AgentDefinition.tenant_id.is_(None)))
        return query.order_by(AgentDefinition.key.asc()).all()

    def update_enabled(self, db: Session, agent_key: str, enabled: bool) -> Optional[AgentDefinition]:
        item = db.query(AgentDefinition).filter(AgentDefinition.key == agent_key).first()
        if not item:
            return None
        item.enabled = enabled
        db.commit()
        db.refresh(item)
        return item
