from dataclasses import dataclass
from typing import Optional

@dataclass
class InterestEvent:
    id: Optional[int]
    tenant_id: Optional[int]
    user_id: Optional[int]
    event_type: str
    channel: str
    content_type: str
    content: str
    timestamp: str
