from abc import ABC 
from dataclasses import dataclass, field 
from uuid import uuid4

from src.domain.common.events.event import Event 

from .enitity import Entity


@dataclass
class AggregateRoot(Entity, ABC):   
    _events: list[Event] = field(default_factory=list, init=False, repr=False, hash=False, compare=False)

    def record_event(self, event: Event) -> None:
        self._events.append(event)
    
    def get_events(self) -> list[Event]:
        return self._events

    def clear_events(self) -> None:
        self._events.clear()
    
    def pull_events(self) -> list[Event]:
        events = self._events.copy()
        self._events.clear()
        return events