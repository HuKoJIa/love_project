from dataclasses import dataclass, field
from typing import Self
from uuid import UUID
from datetime import datetime

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.common.entities.deletable_mixin import DeletableMixin
from src.domain.mirror.category.value_objects.category_id import CategoryId
from src.domain.mirror.photo.value_objects import PhotoId, PhotoDescription, PhotoUrl, CreatedAt, DeletionTime
from src.domain.mirror.photo.events import PhotoCreated, PhotoDeleted, PhotoPuzzled, PhotoCollaged
from src.domain.mirror.photo.exceptions import PhotoIsDeletedError, PhotoAlreadyInPuzzleError

@dataclass
class Puzzle:
    puzzle_id: UUID
    cropped_url: PhotoUrl

@dataclass
class Photo(AggregateRoot, DeletableMixin):
    photo_id: PhotoId
    photo_url: PhotoUrl
    photo_description: PhotoDescription
    category_id: CategoryId
    created_at: CreatedAt = field(default_factory=CreatedAt.value.now, kw_only=True)
    deleted_at: DeletionTime = field(default_factory=DeletionTime.create_not_deleted, kw_only=True)
    puzzles: list[Puzzle] = field(default_factory=list)

    @classmethod
    def create(
        cls,
        photo_id: PhotoId,
        photo_url: PhotoUrl,
        photo_description: PhotoDescription,
        category_id: CategoryId,
    ) -> Self:
        photo = cls(
            photo_id=photo_id,
            photo_url=photo_url,
            photo_description=photo_description,
            category_id=category_id,
        )
        photo.record_event(PhotoCreated(
            photo_id=photo_id.to_raw(),
            photo_url=photo_url.to_raw(),
            photo_description=photo_description.to_raw(),
            category_id=category_id,
        ))
        return photo

    def photo_puzzled(self, puzzle_id: UUID, cropped_url: PhotoUrl) -> None:
        self._validate_not_deleted()
        if any(p.puzzle_id == puzzle_id for p in self.puzzles):
            raise PhotoAlreadyInPuzzleError(self.photo_id, puzzle_id)
        self.puzzles.append(Puzzle(puzzle_id=puzzle_id, cropped_url=cropped_url))
        self.record_event(PhotoPuzzled(
            photo_id=self.photo_id.to_raw(),
            puzzle_id=puzzle_id,
            cropped_url=cropped_url.to_raw(),
        ))

    def add_to_collage(self, collage_id: UUID, collage_url: str) -> None:
        self._validate_not_deleted()
        self.record_event(PhotoCollaged(
            photo_id=self.photo_id.to_raw(),
            collage_id=collage_id,
            collage_url=collage_url,
        ))

    def _get_delete_event(self):
        return PhotoDeleted(self.photo_id)

    def _get_deletion_error(self):
        return PhotoIsDeletedError(self.photo_id.to_raw())