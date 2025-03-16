from dataclasses import dataclass
from src.domain.common.exceptions import DomainError

@dataclass(eq=False)
class ValueObjectError(ValueError, DomainError):
    value: str 
    field_name: str 

    @property
    def title(self) -> str:
        return f"Invalid {self.field_name}"

@dataclass(eq=False)
class EmptyValueError(ValueObjectError):
    @property
    def title(self) -> str:
        return f"{self.field_name} cant be empty"

@dataclass(eq=False)
class TooLongValueError(ValueObjectError):
    @property
    def title(self) -> str:
        return f"Too long {self.field_name}: '{self.value}'"
