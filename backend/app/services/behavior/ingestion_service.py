from app.models.interest_event import InterestEvent

def ingest_behavior_event(db, payload: dict) -> dict:
    event = InterestEvent(**payload)
    db.add(event)
    db.commit()
    db.refresh(event)
    return {"status": "accepted", "id": event.id, "event_type": event.event_type}
