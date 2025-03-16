import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 

@dataclasses.dataclass(frozen=True)
class CollageCreated(Event):
    collage_id: UUID 
    photos_ids: list[UUID]
    collage_url: str
   