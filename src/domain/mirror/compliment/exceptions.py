from dataclasses import dataclass
from uuid import UUID
from src.domain.common.exceptions import DomainError

@dataclass(frozen=True)
class ComplimentError(DomainError):
    compliment_id: UUID
    message: str

    @property
    def title(self) -> str:
        return f"The compliment with {self.compliment_id} {self.message}"

# Конкретные ошибки
@dataclass(frozen=True)
class ComplimentIsDeletedError(ComplimentError):
    def __init__(self, compliment_id: UUID):
        super().__init__(compliment_id, "is deleted")

@dataclass(frozen=True)
class ComplimentAlreadyInactiveError(ComplimentError):
    def __init__(self, compliment_id: UUID):
        super().__init__(compliment_id, "is already inactive")

@dataclass(frozen=True)
class ComplimentActiveCannotDeleteError(ComplimentError):
    def __init__(self, compliment_id: UUID):
        super().__init__(compliment_id, "is active and cannot be deleted")

@dataclass(frozen=True)
class ComplimentExpiredError(ComplimentError):
    def __init__(self, compliment_id: UUID):
        super().__init__(compliment_id, "Compliment is expired 30 days")

