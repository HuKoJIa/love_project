from dataclasses import dataclass, field
from datetime import datetime
from typing import Self 
from uuid import UUID 

from src.domain.common.entities.aggregate_root import AggregateRoot
from src.domain.common.entities.deletable_mixin import DeletableMixin
from src.domain.mirror_support.category.value_objects.category_id import CategoryId
from src.domain.mirror_core.place.events.place_created import PlaceCreated
from src.domain.mirror_core.place.events.place_deleted import PlaceDeleted
from src.domain.mirror_core.place.events.place_highlighed import PlaceHighlighted
from src.domain.mirror_core.place.events.place_unhighlighted import PlaceUnhighlighted
from src.domain.mirror_core.place.events.place_visited import PlaceVisited
from src.domain.mirror_core.place.exceptions import PlaceIsNotHighlightedError, PlaceIsAlreadyHighlightedError, PlaceIsDeletedError
from src.domain.mirror_core.place.value_objects.coordinates import Coordinates
from src.domain.mirror_core.place.value_objects.place_description import PlaceDescription
from src.domain.mirror_core.place.value_objects.place_id import PlaceId
from src.domain.mirror_core.place.value_objects.place_name import PlaceName

@dataclass
class Place(AggregateRoot, DeletableMixin):
    place_id: PlaceId
    place_name: PlaceName
    place_description: PlaceDescription
    place_coordinates: Coordinates | None = None
    category_id: CategoryId
    is_highligted: bool = field(default=False)
   
    
    @classmethod
    def create(cls, place_id: PlaceId, place_name: PlaceName, place_description: PlaceDescription,
            category_id: CategoryId, coordinates: Coordinates | None = None) -> Self:
        place = cls(place_id, place_name, place_description, coordinates, category_id)
        place.record_event(PlaceCreated(place_id=place_id, place_name=place_name,
                                        place_description=place_description, category_id=category_id,
                                        latitude=coordinates.latitude if coordinates else None,
                                        longitude=coordinates.longitude if coordinates else None))
        return place
        
    def visit(self, visit_date: datetime) -> None:
        self._validate_not_deleted()
        self.record_event(PlaceVisited(
            place_id=self.place_id,            
            visit_date=visit_date,
            )
        )
    
    def highlight(self) -> None:        
        self._validate_not_deleted()
        if self.is_highligted:
            raise PlaceIsAlreadyHighlightedError()
        self.is_highligted = True
        self.record_event(PlaceHighlighted(
            place_id=self.place_id,            
        ))

    def unhighlight(self) -> None:
        self._validate_not_deleted()
        if not self.is_highligted:
            raise PlaceIsNotHighlightedError()
        self.is_highligted = False 
        self.record_event(PlaceUnhighlighted(place_id=self.place_id))


    def _get_delete_event(self):
        return PlaceDeleted(self.place_id)

    def _get_deletion_error(self):
        return PlaceIsDeletedError(self.place_id.to_raw())