from dataclasses import dataclass
from typing import Optional

@dataclass
class Consent:
    id: Optional[int]
    tenant_id: Optional[int]
    user_id: Optional[int]
    scope: str
    status: str = "granted"
    retention_days: int = 30
