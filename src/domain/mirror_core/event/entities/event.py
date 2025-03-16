from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Self
from uuid import UUID

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.common.entities.deletable_mixin import DeletableMixin
from src.domain.mirror_support.category.value_objects.category_id import CategoryId
from src.domain.mirror_core.compliment.value_objects.compliment_id import ComplimentId
from src.domain.mirror_core.compliment.value_objects.created_at import CreatedAt
from src.domain.mirror_core.event.events.event_created import EventCreated
from src.domain.mirror_core.event.events.event_deleted import EventDeleted
from src.domain.mirror_core.event.events.event_photo_added import EventPhotoAdded
from src.domain.mirror_core.event.events.event_photo_removed import EventPhotoRemoved
from src.domain.mirror_core.event.exceptions import EventIsDeletedError
from src.domain.mirror_core.event.value_objects.event_description import EventDescription
from src.domain.mirror_core.event.value_objects.event_id import EventId
from src.domain.mirror_core.event.value_objects.event_title import EventTitle
from src.domain.mirror_core.music.value_objects.music_id import MusicId
from src.domain.mirror_core.photo.value_objects.photo_id import PhotoId
from src.domain.mirror_core.place.value_objects.place_id import PlaceId



@dataclass
class Event(AggregateRoot, DeletableMixin):
    event_id: EventId
    title: EventTitle
    date: CreatedAt
    description: EventDescription
    category_id: CategoryId
    place_id: PlaceId | None = None 
    photo_ids: list[PhotoId] = field(default_factory=list)
    music_id: MusicId | None = None 
    compliment_id: ComplimentId | None = None
   

    @classmethod
    def create(
            cls, 
            event_id: EventId,
            title: EventTitle,
            date: CreatedAt,
            description: EventDescription,
            category_id: CategoryId,
            place_id: PlaceId | None = None,
            photo_ids: list[PhotoId] | None = None,
            music_id: MusicId | None = None,
            compliment_id: ComplimentId | None = None            
               ) -> Self:
        
        event = cls(
            event_id=event_id, 
            title=title,
            date=date,
            description=description,
            category_id=category_id,
            place_id=place_id,
            photo_ids=photo_ids or [],
            music_id=music_id,
            compliment_id=compliment_id,
            )
        event.record_event(EventCreated(
            event_id=event_id, 
            title=title,
            date=date,
            description=description,
            category_id=category_id,
            place_id=place_id,
            photo_ids=photo_ids or [],
            music_id=music_id,
            compliment_id=compliment_id,
        ))
        return event
    
    def add_photo(self, photo_id: PhotoId) -> None:
        if photo_id not in self.photo_ids:
            self.photo_ids.append(photo_id)
            self.record_event(EventPhotoAdded(event_id=self.event_id, photo_id=photo_id))

    def remove_photo(self, photo_id: PhotoId) -> None:
        if photo_id in self.photo_ids:
            self.photo_ids.remove(photo_id)
            self.record_event(EventPhotoRemoved(event_id=self.event_id, photo_id=photo_id))

    def _get_delete_event(self) -> EventDeleted:
        return EventDeleted(self.event_id)
    

    def _get_deletion_error(self) -> EventIsDeletedError:
        return EventIsDeletedError(self.event_id.to_raw())
    

