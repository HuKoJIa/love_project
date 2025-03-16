import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 

@dataclasses.dataclass(frozen=True)
class PhotoPuzzled(Event):
    photo_id: UUID 
    puzzle_id: str 
    cropped_url: str | None = None 
    