import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 


@dataclasses.dataclass(frozen=True)
class CategoryCreated(Event):
    category_id: UUID
    name: str   
    description: str
    