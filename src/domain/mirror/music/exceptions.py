from dataclasses import dataclass
from uuid import UUID
from src.domain.common.exceptions import DomainError

@dataclass(frozen=True)
class MusicIsDeletedError(DomainError):
    music_id: UUID
   

    @property
    def title(self) -> str:
        return f"The music with {self.music_id} is deleted"

