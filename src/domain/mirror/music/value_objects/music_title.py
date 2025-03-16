from uuid import UUID 
from dataclasses import dataclass
from src.domain.common.exceptions.value_objects_exceptions import EmptyValueError, TooLongValueError


from src.domain.common.value_objets import ValueObject


MAX_TITLE_LENGHT = 100



@dataclass(frozen=True)
class MusicTitle(ValueObject[str]):
    value: str 

    def _validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyValueError(self.value, "title")
        if len(self.value) > MAX_TITLE_LENGHT:
            raise TooLongValueError(self.value, "title")
     