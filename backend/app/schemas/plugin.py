from pydantic import BaseModel
from typing import List

class PluginOut(BaseModel):
    slug: str
    name: str
    version: str
    approved: bool
    installed: bool

class PluginRescanResponse(BaseModel):
    discovered: List[str]
