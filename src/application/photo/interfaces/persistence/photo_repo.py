import abc 
from typing import Protocol

from src.domain.mirror.photo import entities
from src.domain.mirror.photo.value_objects.photo_id import PhotoId


class PhotoRepo(Protocol):
    @abc.abstractmethod
    async def acquire_photo_by_id(self, photo_id: PhotoId) -> entities.Photo:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def add_photo(self, photo: entities.Photo) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def update_photo(self, photo: entities.Photo) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def delete_photo(self, photo_id: PhotoId) -> None:
        raise NotImplementedError
    