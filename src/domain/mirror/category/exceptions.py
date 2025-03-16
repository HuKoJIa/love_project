from dataclasses import dataclass
from uuid import UUID
from src.domain.common.exceptions import DomainError

@dataclass(frozen=True)
class CategoryIsDeletedError(DomainError):
    category_id: UUID
   

    @property
    def title(self) -> str:
        return f"The category with {self.category_id} is deleted"

