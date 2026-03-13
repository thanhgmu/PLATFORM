from dataclasses import dataclass
from typing import Optional

@dataclass
class AuditLog:
    id: Optional[int]
    actor: str
    action: str
    tenant_id: Optional[int]
    resource_type: str
    resource_id: Optional[str]
    timestamp: str
