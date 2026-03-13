from pydantic import BaseModel

class BehaviorEventIn(BaseModel):
    tenant_id: int | None = None
    user_id: int | None = None
    event_type: str
    channel: str
    content_type: str
    content: str
    timestamp: str

class RecommendationOut(BaseModel):
    user_id: int | None = None
    preferred_channels: list[str]
    next_best_action: str
    topic_tags: list[str]
