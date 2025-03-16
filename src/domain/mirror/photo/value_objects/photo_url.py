import re 
from dataclasses import dataclass
from src.domain.common.exceptions.value_objects_exceptions import EmptyValueError, TooLongValueError, ValueObjectError
from src.domain.common.value_objets.base import ValueObject



MAX_URL_LENGHT = 255 
URL_PATTERN = re.compile(r'^https?://[\w\-\.]+(:d+)?(/[\w\-\./]*)*$')

@dataclass(eq=False)
class WrongUrlFormatError(ValueObjectError):
    @property
    def title(self) -> str:
        return f"Wrong {self.f} format: '{self.value}'"
    
@dataclass(frozen=True)
class PhotoUrl(ValueObject[str]):
    value: str 
    
    def _validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyValueError(self.value, "URL")
        if len(self.value) > MAX_URL_LENGHT:
            raise TooLongValueError(self.value, "URL")
        if not URL_PATTERN.match(self.value):
            raise WrongUrlFormatError(self.value, "URL")
