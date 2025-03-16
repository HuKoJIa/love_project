import dataclasses
import datetime
from uuid import UUID

from src.domain.common.events.event import Event 


@dataclasses.dataclass(frozen=True)
class EventPhotoAdded(Event):
    event_id: UUID
    photo_id: UUID   