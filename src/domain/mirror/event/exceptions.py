from dataclasses import dataclass
from uuid import UUID
from src.domain.common.exceptions import DomainError

@dataclass(frozen=True)
class EventIsDeletedError(DomainError):
   event_id: UUID  
   
   @property
   def title(self) -> str:
      return f"The event with {self.event_id} is deleted"
