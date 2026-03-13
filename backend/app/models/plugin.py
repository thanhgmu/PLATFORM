from dataclasses import dataclass
from typing import Optional

@dataclass
class Plugin:
    id: Optional[int]
    slug: str
    name: str
    version: str
    approved: bool = False
    installed: bool = False
