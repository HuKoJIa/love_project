import re 
from dataclasses import dataclass
from src.domain.common.exceptions.value_objects_exceptions import EmptyValueError, TooLongValueError, ValueObjectError
from src.domain.common.value_objets.base import ValueObject



MAX_URL_LENGHT = 100 
URL_PATTERN = re.compile(r'^[a-zA-Z]+$')


@dataclass(eq=False)
class WrongNameFormatError(ValueObjectError):
    @property
    def title(self) -> str:
        return f"Wrong {self.field_name} format:' {self.value}'"
    
@dataclass(frozen=True)
class CategoryName(ValueObject[str]):
    value: str 
    
    def _validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyValueError(self.value, "name")
        if len(self.value) > MAX_URL_LENGHT:
            raise TooLongValueError(self.value, "name")
        if not URL_PATTERN.match(self.value):
            raise WrongNameFormatError(self.value, "name")
