from typing import TypeAlias

from src.application.common.pagination.dto import PaginatedTeimsDTO

from .deleted_photo import DeletedPhoto
from .photo import Photo

PhotoDTOs: TypeAlias = Photo | DeletedPhoto
Photos: TypeAlias = PaginatedTeimsDTO[PhotoDTOs]