from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Self
from uuid import UUID

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.common.entities.deletable_mixin import DeletableMixin
from src.domain.mirror.category.value_objects.category_id import CategoryId
from src.domain.mirror.music.events.music_created import MusicCreated
from src.domain.mirror.music.events.music_deleted import MusicDeleted
from src.domain.mirror.music.events.music_marked import MusicMarkedAsFavorite
from src.domain.mirror.music.events.music_unmarked import MusicUnmarkedAsFavorite
from src.domain.mirror.music.exceptions import MusicIsDeletedError
from src.domain.mirror.music.value_objects.music_artist import MusicArtist
from src.domain.mirror.music.value_objects.music_title import MusicTitle
from src.domain.mirror.music.value_objects.music_id import MusicId
from src.domain.mirror.music.value_objects.music_url import MusicUrl




@dataclass
class Music(AggregateRoot, DeletableMixin):
    music_id: MusicId
    title: MusicTitle
    artist: MusicArtist | None
    category_id: CategoryId
    music_url: MusicUrl
    is_favorite: bool = False 
   

    @classmethod
    def create(cls, 
               music_id: MusicId, 
               title: MusicTitle,
               artist: MusicArtist,
               music_url: MusicUrl,
               is_favorite: bool = False,
               ) -> Self:
        music = cls(
            music_id=music_id, 
            title=title,
            artist=artist,
            music_url=music_url,
            is_favorite=is_favorite,
            )
        music.record_event(MusicCreated(
            music_id=music_id,
            title=title,
            artist=artist,
            music_url=music_url,
            is_favorite=is_favorite,
        ))
        return music
    


    def mark_as_favorite(self) -> None:
        self._validate_not_deleted()
        if not self.is_favorite:
            self.is_favorite = True 
            self.record_event(MusicMarkedAsFavorite(music_id=self.music_id))
        
   
    def unmark_as_favorite(self) -> None:
         self._validate_not_deleted()
         if self.is_favorite:
             self.is_favorite = False 
             self.record_event(MusicUnmarkedAsFavorite(music_id=self.music_id))



    def _get_delete_event(self) -> MusicDeleted:
        return MusicDeleted(self.music_id)
    

    def _get_deletion_error(self) -> MusicIsDeletedError:
        return MusicIsDeletedError(self.music_id.to_raw())
    

