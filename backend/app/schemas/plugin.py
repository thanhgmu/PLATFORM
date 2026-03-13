from pydantic import BaseModel

class PluginOut(BaseModel):
    slug: str
    name: str
    version: str
    approved: bool
    installed: bool
