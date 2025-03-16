import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 
from src.domain.mirror.place.value_objects import Coordinates

@dataclasses.dataclass(frozen=True)
class PlaceUnhighlighted(Event):
    place_id: UUID
  