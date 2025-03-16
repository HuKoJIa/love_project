from dataclasses import dataclass, field 
from uuid import UUID 

from src.application.common.dto import DTO
from src.domain.mirror.photo.entities.photo import Puzzle 


@dataclass(frozen=True)
class Photo(DTO):
    photo_id: UUID 
    photo_url: str 
    photo_description: str 
    category_id: UUID 
    puzzles: list[Puzzle]

