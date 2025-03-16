from dataclasses import dataclass
from typing import Protocol
from uuid import UUID 

from src.application.common.pagination.dto import Pagination
from src.application.photo import dto 
from src.domain.common.constants import Empty 

@dataclass(frozen=True)
class GetPhotoFilters:
    deleted: bool | Empty = Empty.UNSET


class PhotoReader(Protocol):
    async def get_photo_by_id(self, photo_id: UUID) -> dto.PhotoDTOs:
        raise NotImplementedError
    
    async def get_photos(self, filters: GetPhotoFilters, pagination: Pagination) -> dto.Photos:
        raise NotImplementedError

    async def get_photo_categories(self, cateogry_id: UUID) -> dto.PhotoDTOs:
        raise NotImplementedError
    