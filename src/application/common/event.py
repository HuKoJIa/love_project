from abc import ABC 
from typing import Generic, TypeVar

import didiator

from src.domain.common.events import Event 


E = TypeVar("E", bound=Event)

class EventHanlder(didiator.EventHandler[E], ABC, Generic[E]):
    pass 
