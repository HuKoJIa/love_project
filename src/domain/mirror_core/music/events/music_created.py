import dataclasses
from uuid import UUID

from src.domain.common.events.event import Event 


@dataclasses.dataclass(frozen=True)
class MusicCreated(Event):
    music_id: UUID
    title: str
    artist: str | None
    music_url: str
    is_favorite: bool