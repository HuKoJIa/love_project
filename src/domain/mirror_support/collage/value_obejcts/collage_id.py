from uuid import UUID, uuid4
from dataclasses import dataclass, field

from src.domain.common.value_objets import ValueObject

@dataclass(frozen=True)
class CollageId(ValueObject[UUID]):
    value: UUID
 