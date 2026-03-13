from dataclasses import dataclass
from typing import Optional

@dataclass
class Tenant:
    id: Optional[int]
    name: str
    owner_user_id: Optional[int] = None
