from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Self
from uuid import UUID

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.common.entities.deletable_mixin import DeletableMixin
from src.domain.mirror.category.events.category_created import CategoryCreated
from src.domain.mirror.category.events.category_deleted import CategoryDeleted
from src.domain.mirror.category.exceptions import CategoryIsDeletedError
from src.domain.mirror.category.value_objects.category_description import CategoryDescription
from src.domain.mirror.category.value_objects.category_id import CategoryId
from src.domain.mirror.category.value_objects.category_name import CategoryName




@dataclass
class Category(AggregateRoot, DeletableMixin):
    category_id: CategoryId
    name: CategoryName
    description: CategoryDescription
   
   

    @classmethod
    def create(cls, 
               category_id: CategoryId, 
               name: CategoryName,
               description: CategoryDescription,              
               ) -> Self:
        category = cls(
            category_id=category_id, 
            name=name,
            description=description, 
           
            )
        category.record_event(CategoryCreated(
            category_id=category_id,
            name=name,
            description=description,
          
        ))
        return category
    




    def _get_delete_event(self) -> CategoryDeleted:
        return CategoryDeleted(self.category_id)
    

    def _get_deletion_error(self) -> CategoryIsDeletedError:
        return CategoryIsDeletedError(self.category_id.to_raw())
    

