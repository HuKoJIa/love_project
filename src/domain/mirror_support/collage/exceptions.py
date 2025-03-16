from dataclasses import dataclass
from uuid import UUID

from src.domain.common.exceptions.base import DomainError


@dataclass(eq=False)
class PhotoAlreadyInCollageError(DomainError):
    photo_id: UUID
    collage_id: UUID 

    @property
    def title(self) -> str:
        return f"Photo '{self.photo_id}' is already included in collage '{self.collage_id}'"

class CollageCapacityExceededError(DomainError):
    collage_id: UUID

    @property
    def title(self) -> str:
        return f"Collage '{self.collage_id}' cannot contain more than 3 photos"