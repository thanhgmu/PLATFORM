class OpenClawAdapter:
    """Adapter boundary between Platform Core and OpenClaw runtime.

    TODO Phase 2:
    - replace placeholder responses with HTTP/webhook integration
    - add tenant-scoped and user-scoped workspace routing
    - add signed requests and audit hooks
    """

    def ingest_event(self, event: dict) -> dict:
        return {
            "status": "accepted",
            "source": "openclaw",
            "event": event,
        }

    def send_message(self, payload: dict) -> dict:
        return {
            "status": "queued",
            "source": "openclaw",
            "payload": payload,
        }

    def get_context(self, payload: dict) -> dict:
        return {
            "tenant": {"id": payload.get("tenant_id"), "plan": "pro"},
            "user": {"id": payload.get("user_id"), "role": "user"},
            "tools": ["report.read", "message.reply"],
            "features": {"behavioral_personalization": True},
        }
