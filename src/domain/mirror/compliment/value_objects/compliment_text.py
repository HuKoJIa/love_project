from dataclasses import dataclass


from src.domain.common.exceptions.value_objects_exceptions import EmptyValueError, TooLongValueError
from src.domain.common.value_objets.base import ValueObject

MAX_DESCRIPTION_LENGTH = 255

@dataclass(frozen=True)
class ComplimentText(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyValueError(self.value, "Text")
        if len(self.value) > MAX_DESCRIPTION_LENGTH:
            raise TooLongValueError(self.value, "Text")

