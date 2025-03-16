import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 
from src.domain.mirror_core.place.value_objects import Coordinates

@dataclasses.dataclass(frozen=True)
class PlaceCreated(Event):
    place_id: UUID 
    place_name: str 
    place_descrption: str 
    category_id: UUID
    latitude: float | None = None
    longitude: float | None = None

