import dataclasses
from uuid import UUID
from datetime import datetime

from src.domain.common.events.event import Event 
from src.domain.mirror.place.value_objects import Coordinates

@dataclasses.dataclass(frozen=True)
class PlaceVisited(Event):
    place_id: UUID
    visit_date: datetime
