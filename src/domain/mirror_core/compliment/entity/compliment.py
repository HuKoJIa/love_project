from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Self
from uuid import UUID

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.common.entities.deletable_mixin import DeletableMixin
from src.domain.mirror_support.category.value_objects.category_id import CategoryId
from src.domain.mirror_core.compliment.events.compliement_created import ComplimentCreated
from src.domain.mirror_core.compliment.events.compliment_deactivated import ComplimentDeactivated
from src.domain.mirror_core.compliment.events.compliment_deleted import ComplimentDeleted
from src.domain.mirror_core.compliment.events.compliment_used import ComplimentUsed
from src.domain.mirror_core.compliment.exceptions import ComplimentActiveCannotDeleteError, ComplimentAlreadyInactiveError, ComplimentExpiredError, ComplimentIsDeletedError
from src.domain.mirror_core.compliment.value_objects.compliment_id import ComplimentId
from src.domain.mirror_core.compliment.value_objects.compliment_text import ComplimentText
from src.domain.mirror_core.compliment.value_objects.created_at import CreatedAt




@dataclass
class Compliment(AggregateRoot, DeletableMixin):
    compliment_id: ComplimentId
    compliment_text: ComplimentText
    category_id: CategoryId
    is_active: bool = True
    created_at: CreatedAt
    expiration_period: timedelta = timedelta(days=30)


    @classmethod
    def create(cls, compliment_id: ComplimentId, compliment_text: ComplimentText, category_id: CategoryId) -> Self:
        compliment = cls(compliment_id, compliment_text, category_id)
        compliment.record_event(ComplimentCreated(
            compliment_id=compliment_id,
            compliment_text=compliment_text,
            category_id=category_id,
        ))
        return compliment
        
   
    
    def deactivate(self, force: bool = False) -> None:
        if not self.is_active and not force:
            raise ComplimentAlreadyInactiveError(self.compliment_id.to_raw())
        self.is_active = False
        self.record_event(ComplimentDeactivated(self.compliment_id.to_raw()))

    def delete(self) -> None:
        self._validate_not_deleted()
        if self.is_active:
           raise ComplimentActiveCannotDeleteError(self.compliment_id.to_raw())
        super().delete()

    def is_expired(self, current_time: datetime = datetime.now()) -> bool:
        return current_time > self.created_at + self.expiration_period    
    
    def use(self) -> None:
        self._validate_not_deleted()
        if self.is_expired():
            raise ComplimentExpiredError(self.compliment_id.to_raw())
        self.record_event(ComplimentUsed(self.compliment_id))
        self.deactivate()

    def _get_delete_event(self) -> ComplimentDeleted:
        return ComplimentDeleted(self.compliment_id)
    

    def _get_deletion_error(self) -> ComplimentIsDeletedError:
        return ComplimentIsDeletedError(self.compliment_id.to_raw())
    

#Добавить возможность создания коммплиментов с помощью AI grok 