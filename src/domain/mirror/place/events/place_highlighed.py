import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 
from src.domain.mirror.place.value_objects import Coordinates

@dataclasses.dataclass(frozen=True)
class PlaceHighlighted(Event):
    place_id: UUID
  