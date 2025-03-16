import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 

@dataclasses.dataclass(frozen=True)
class PhotoCollaged(Event):
    photo_id: UUID
    collage_id: str 
    collage_url: str | None = None