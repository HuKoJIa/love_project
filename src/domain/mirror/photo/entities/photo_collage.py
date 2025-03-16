from dataclasses import dataclass, field
from typing import Self 
from uuid import UUID 


from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.mirror.photo.events.collage_photo_add import CollagePhotoAdded
from src.domain.mirror.photo.value_objects import PhotoId,  PhotoUrl
from src.domain.mirror.photo.events import CollageCreated
from src.domain.mirror.photo.exceptions import PhotoAlreadyInCollageError, CollageCapacityExceededError

class Collage(AggregateRoot):
    collage_id: UUID 
    photos_ids: list[PhotoId] = field(default_factory=list)
    collage_url: PhotoUrl 

    @classmethod
    def create(cls, collage_id: UUID, photo_ids: list[PhotoId], collage_url: PhotoUrl) -> Self:
        collage = cls(collage_id=collage_id, photo_ids=photo_ids, collage_url=collage_url)
        collage.record_event(CollageCreated(
            collage_id=collage_id,
            photos_ids=[photo_id.to_raw() for photo_id in photo_ids],
            collage_url=collage_url.to_raw() if collage_url else None,
        ))
        return collage
    
    def add_photo(self, photo_id: PhotoId) -> None:
        if photo_id in self.photos_ids:
            raise PhotoAlreadyInCollageError(photo_id.to_raw(), self.collage_id)
        if len(self.photos_ids) >= 3:
            raise CollageCapacityExceededError(self.collage_id)
        self.photos_ids.append(photo_id)
        self.record_event(CollagePhotoAdded(
            collage_id=self.collage_id,
            photo_id=photo_id.to_raw(),
        ))
            