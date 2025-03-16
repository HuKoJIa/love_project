from uuid import UUID 
from dataclasses import dataclass
from src.domain.common.exceptions.value_objects_exceptions import EmptyValueError, TooLongValueError


from src.domain.common.value_objets import ValueObject


MAX_DESCRIPTION_LENGHT = 255



@dataclass(frozen=True)
class EventDescription(ValueObject[str]):
    value: str 

    def _validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyValueError(self.value, "description")
        if len(self.value) > MAX_DESCRIPTION_LENGHT:
            raise TooLongValueError(self.value, "description")
     