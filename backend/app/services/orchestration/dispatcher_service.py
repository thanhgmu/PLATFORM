from typing import Any, Dict


class DispatcherService:
    def dispatch(self, agent_key: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "agent_key": agent_key,
            "status": "accepted",
            "payload_echo": payload,
        }
