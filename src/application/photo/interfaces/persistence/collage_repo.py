import abc 
from typing import Protocol
from uuid import UUID

from src.domain.mirror.photo import entities
from src.domain.mirror.photo.value_objects.photo_id import PhotoId


class CollageRepo(Protocol):
    @abc.abstractmethod
    async def get_collage_by_id(self, photo_id: PhotoId) -> entities.Collage:
        raise NotImplementedError

    @abc.abstractmethod
    async def add_collage(self, collage_id: UUID) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def update_collage(self, collage: entities.Collage) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def delete_collage(self, collage_id: UUID) -> None:
        raise NotImplementedError
    