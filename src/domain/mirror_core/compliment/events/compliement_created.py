import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 


@dataclasses.dataclass(frozen=True)
class ComplimentCreated(Event):
    compliment_id: UUID
    compliment_text: str
    category_id: UUID
   