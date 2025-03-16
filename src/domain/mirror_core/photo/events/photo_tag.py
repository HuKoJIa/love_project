import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 

@dataclasses.dataclass(frozen=True)
class PhotoTagged(Event):
    photo_id: UUID 
    tag: str 
    