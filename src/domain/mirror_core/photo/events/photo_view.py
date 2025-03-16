import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 

@dataclasses.dataclass(frozen=True)
class PhotoViewed(Event):
    photo_id: UUID 
    viewad_at: str 
    