from dataclasses import dataclass, field
from typing import Self 



from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.mirror_support.collage.events.collage_created import CollageCreated
from src.domain.mirror_support.collage.events.collage_photo_add import CollagePhotoAdded
from src.domain.mirror_core.photo.value_objects import PhotoId
from src.domain.mirror_support.collage.exceptions import CollageCapacityExceededError, PhotoAlreadyInCollageError
from src.domain.mirror_support.collage.value_obejcts.collage_id import CollageId
from src.domain.mirror_support.collage.value_obejcts.collage_url import CollageUrl

class Collage(AggregateRoot):
    collage_id: CollageId 
    photos_ids: list[PhotoId] = field(default_factory=list)
    collage_url: CollageUrl 

    @classmethod
    def create(cls, collage_id: CollageId, photo_ids: list[PhotoId], collage_url: CollageUrl) -> Self:
        collage = cls(collage_id=collage_id, photo_ids=photo_ids, collage_url=collage_url)
        collage.record_event(CollageCreated(
            collage_id=collage_id,
            photos_ids=[photo_id for photo_id in photo_ids],
            collage_url=collage_url if collage_url else None,
        ))
        return collage
    
    def add_photo(self, photo_id: PhotoId) -> None:
        if photo_id in self.photos_ids:
            raise PhotoAlreadyInCollageError(photo_id, self.collage_id)
        if len(self.photos_ids) >= 3:
            raise CollageCapacityExceededError(self.collage_id)
        self.photos_ids.append(photo_id)
        self.record_event(CollagePhotoAdded(
            collage_id=self.collage_id,
            photo_id=photo_id,
        ))
            