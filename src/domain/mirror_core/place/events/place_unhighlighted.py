import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 

@dataclasses.dataclass(frozen=True)
class PlaceUnhighlighted(Event):
    place_id: UUID
  