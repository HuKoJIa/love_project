from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=False)
class AppError(Exception):
    status: ClassVar[int] = 500

    @property
    def title(self) -> str:
        return "An app error occurred"

class DomainError(AppError):
    @property
    def title(self) -> str:
        return "A domain error occurred"