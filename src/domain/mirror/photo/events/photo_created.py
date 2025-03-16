import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 

@dataclasses.dataclass(frozen=True)
class PhotoCreated(Event):
    photo_id: UUID 
    photo_url: str 
    description: str 
    category_id: UUID
    