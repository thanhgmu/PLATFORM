from app.core.config import settings

class OpenClawAdapter:
    """Adapter boundary between Platform Core and OpenClaw runtime.

    This remains a placeholder-by-contract adapter:
    - safe to update independently of Platform Core
    - no direct DB mutations
    - all actions should be audited by calling services
    """

    def __init__(self):
        self.base_url = settings.OPENCLAW_BASE_URL
        self.enabled = settings.OPENCLAW_ENABLED

    def ingest_event(self, event: dict) -> dict:
        return {
            "status": "accepted" if self.enabled else "disabled",
            "source": "openclaw",
            "base_url": self.base_url,
            "event": event,
        }

    def send_message(self, payload: dict) -> dict:
        return {
            "status": "queued" if self.enabled else "disabled",
            "source": "openclaw",
            "base_url": self.base_url,
            "payload": payload,
        }

    def get_context(self, payload: dict) -> dict:
        return {
            "tenant": {"id": payload.get("tenant_id"), "plan": "pro"},
            "user": {"id": payload.get("user_id"), "role": "user"},
            "tools": ["report.read", "message.reply"],
            "features": {
                "behavioral_personalization": True,
                "openclaw_enabled": self.enabled,
            },
        }
