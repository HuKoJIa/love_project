import dataclasses
from uuid import UUID
from datetime import datetime

from src.domain.common.events.event import Event 

@dataclasses.dataclass(frozen=True)
class PlaceVisited(Event):
    place_id: UUID
    visit_date: datetime
