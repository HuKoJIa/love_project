import re 
from dataclasses import dataclass
from src.domain.common.exceptions.value_objects_exceptions import EmptyValueError, TooLongValueError, ValueObjectError
from src.domain.common.value_objets.base import ValueObject



MAX_URL_LENGHT = 100 
URL_PATTERN = re.compile(r'^[a-zA-Z]+$')


@dataclass(eq=False)
class WrongEventFormatError(ValueObjectError):
    @property
    def title(self) -> str:
        return f"Wrong {self.field_name} format:' {self.value}'"
    
@dataclass(frozen=True)
class EventTitle(ValueObject[str]):
    value: str 
    
    def _validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyValueError(self.value, "event")
        if len(self.value) > MAX_URL_LENGHT:
            raise TooLongValueError(self.value, "event")
        if not URL_PATTERN.match(self.value):
            raise WrongEventFormatError(self.value, "event")
