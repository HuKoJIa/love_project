from uuid import UUID 
from dataclasses import dataclass
from src.domain.common.exceptions.value_objects_exceptions import EmptyValueError, TooLongValueError

from src.domain.common.value_objets import ValueObject

MAX_ARTISTNAME_LENGHT = 100


@dataclass(frozen=True)
class MusicArtist(ValueObject[str]):
    value: str 

    def _validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyValueError(self.value, "artistname")
        if len(self.value) > MAX_ARTISTNAME_LENGHT:
            raise TooLongValueError(self.value, "artistname")
     