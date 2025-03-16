import dataclasses
import datetime
from uuid import UUID

from src.domain.common.events.event import Event 


@dataclasses.dataclass(frozen=True)
class EventCreated(Event):
    event_id: UUID
    title: str
    date: datetime
    description: str
    place_id: UUID | None = None
    photo_ids: list[UUID]
    music_id: UUID | None = None
    compliment_id: UUID | None = None
