import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event



@dataclasses.dataclass(frozen=True)
class CollagePhotoAdded(Event):
    collage_id: UUID
    photo_id: UUID