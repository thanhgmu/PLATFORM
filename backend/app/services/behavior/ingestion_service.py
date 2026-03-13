_EVENTS: list[dict] = []

def ingest_behavior_event(payload: dict) -> dict:
    _EVENTS.append(payload)
    return {"status": "accepted", "count": len(_EVENTS), "event": payload}
