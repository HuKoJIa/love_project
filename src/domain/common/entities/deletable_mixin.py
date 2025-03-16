from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from src.domain.common.value_objets.deleted_status import DeletionTime
from src.domain.common.entities.aggregate_root import AggregateRoot


class DeletableMixin(ABC):
    deleted_at = field(default_factory=DeletionTime.create_not_deleted(),kw_only=True)

    def _validate_not_deleted(self) -> None:
        if self.deleted_at.is_deleted():
            raise self._get_deletion_error()
    
    def delete(self) -> None:
        self._validate_not_deleted()
        self.deleted_at = DeletionTime.create_deleted()
        self.record_event(self._get_delete_event())
    
    @abstractmethod
    def _get_delete_event(self):
        pass 

    @abstractmethod
    def _get_deletion_error(self):
        pass