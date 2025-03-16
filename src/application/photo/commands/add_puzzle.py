import logging 
from dataclasses import dataclass
from uuid import UUID 

from didiator import EventMediator
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.uow import UnitOfWork
from src.application.photo.interfaces import PhotoRepo
from src.domain.mirror.photo.value_objects import PhotoId, PhotoUrl

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class AddPuzzleToPhoto(Command[None]):
    photo_id: UUID
    puzzle_id: UUID
    cropped_url: str

class AddPuzzleToPhotoHandler(CommandHandler[AddPuzzleToPhoto, None]):
    def __init__(self, photo_repo: PhotoRepo, uow: UnitOfWork, mediator: EventMediator):
        self._photo_repo = photo_repo
        self._uow = uow 
        self._mediator = mediator
    
    async def __call__(self, command: AddPuzzleToPhoto) -> None:
        photo_id = PhotoId(command.photo_id)
        cropped_url = PhotoUrl(command.cropped_url)

        photo = await self._photo_repo.acquire_photo_by_id(photo_id)
        photo.photo_puzzled(command.puzzle_id, cropped_url)
        await self._photo_repo.update_photo(photo)
        await self._mediator.publish(photo.pull_events())
        await self._uow.commit()

        logger.info("Puzzle added to photo", extra={"photo_id": photo_id.to_raw()})