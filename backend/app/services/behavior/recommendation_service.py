import json
from app.models.interest_event import InterestEvent
from app.models.recommendation import Recommendation

def get_recommendation(db, user_id: int | None) -> dict:
    events = db.query(InterestEvent).filter(InterestEvent.user_id == user_id).all()

    channels = {}
    tags = {}

    for event in events:
        channels[event.channel] = channels.get(event.channel, 0) + 1
        for token in (event.content or "").lower().split():
            if len(token) < 4:
                continue
            tags[token] = tags.get(token, 0) + 1

    preferred_channels = sorted(channels, key=channels.get, reverse=True)[:3]
    topic_tags = sorted(tags, key=tags.get, reverse=True)[:5]

    existing = db.query(Recommendation).filter(Recommendation.user_id == user_id).first()
    if existing:
        existing.preferred_channels = json.dumps(preferred_channels)
        existing.topic_tags = json.dumps(topic_tags)
        existing.next_best_action = "send_contextual_followup"
        db.commit()
        return {
            "user_id": user_id,
            "preferred_channels": preferred_channels,
            "next_best_action": existing.next_best_action,
            "topic_tags": topic_tags,
        }

    rec = Recommendation(
        user_id=user_id,
        preferred_channels=json.dumps(preferred_channels),
        next_best_action="send_contextual_followup",
        topic_tags=json.dumps(topic_tags),
    )
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return {
        "user_id": user_id,
        "preferred_channels": preferred_channels,
        "next_best_action": rec.next_best_action,
        "topic_tags": topic_tags,
    }
