from uuid import UUID 
from dataclasses import dataclass

from src.domain.common.value_objets import ValueObject

@dataclass(frozen=True)
class CategoryId(ValueObject[UUID]):
    value: UUID 

 