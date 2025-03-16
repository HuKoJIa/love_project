from uuid import UUID 
from dataclasses import dataclass

from src.domain.common.value_objets import ValueObject

@dataclass(frozen=True)
class MusicId(ValueObject[UUID]):
    value: UUID 

 