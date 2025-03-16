from dataclasses import dataclass
from uuid import UUID 

from src.domain.common.exceptions import DomainError


@dataclass(eq=False)
class PlaceIsDeletedError(RuntimeError, DomainError):
    place_id: UUID 

    @property
    def title(self) -> str:
        return f'The place with {self.place_id} place_id is deleted'

@dataclass(eq=False)
class PlaceIsAlreadyHighlightedError(DomainError):
    
    @property
    def title(self) -> str:
        return 'Place is already highlighted'

@dataclass(eq=False)
class PlaceIsNotHighlightedError(DomainError):
    @property
    def title(self) -> str:
        return 'Place is not highlighted'

