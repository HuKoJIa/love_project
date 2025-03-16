from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from src.application.common.dto import DTO
from src.domain.mirror.photo.entities.photo import Puzzle 

@dataclass(frozen=True)
class DeletedPhoto(DTO):
    photo_id: UUID 
    photo_url: str 
    photo_description: str 
    category_id: UUID 
 

