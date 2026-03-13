from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Recommendation:
    id: Optional[int]
    tenant_id: Optional[int]
    user_id: Optional[int]
    channels: List[str]
    next_best_action: str
    topic_tags: List[str]
