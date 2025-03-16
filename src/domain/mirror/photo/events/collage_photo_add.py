import dataclasses
from uuid import UUID



@dataclasses.dataclass(frozen=True)
class CollagePhotoAdded:
    collage_id: UUID
    photo_id: UUID