from dataclasses import dataclass
from uuid import UUID 

from src.domain.common.exceptions import DomainError


@dataclass(eq=False)
class PhotoIsDeletedError(RuntimeError, DomainError):
    photo_id: UUID 

    @property
    def title(self) -> str:
        return f'The photo with {self.photo_id} photo_id is deleted'
    
@dataclass(eq=False)
class PhotoAlreadyExistsError(DomainError):
    photo_url: str | None = None 

    @property
    def title(self) -> str:
        if self.photo_url is None:
            return "Photo with photo_url already exists"
        return f'A photo with the "{self.photo_url}" photo_url alreadt exists'
    

@dataclass(eq=False)
class PhotoAlreadyInPuzzleError(DomainError):
    photo_id: UUID
    puzzle_id: UUID

    @property
    def title(self) -> str:
        return f"Photo '{self.photo_id}' is already assigned to puzzle '{self.puzzle_id}'"

