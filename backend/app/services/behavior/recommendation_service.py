from app.services.behavior.ingestion_service import _EVENTS
from app.services.behavior.interest_scoring_service import score_interests

def get_recommendation(user_id: int | None) -> dict:
    user_events = [e for e in _EVENTS if e.get("user_id") == user_id]
    scored = score_interests(user_events)
    return {
        "user_id": user_id,
        "preferred_channels": scored.get("preferred_channels", []),
        "next_best_action": "send_contextual_followup",
        "topic_tags": scored.get("topic_tags", []),
    }
