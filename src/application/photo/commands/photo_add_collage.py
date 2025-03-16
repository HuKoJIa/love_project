import logging 
from dataclasses import dataclass
from uuid import UUID 

from didiator import EventMediator
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.uow import UnitOfWork
from src.application.photo.interfaces import PhotoRepo
from src.application.photo.interfaces.persistence.collage_repo import CollageRepo
from src.domain.mirror_core.photo.value_objects import PhotoId, PhotoUrl

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class AddPhotoToCollage(Command[None]):
    photo_id: UUID 
    collage_id: UUID
    collage_url: str 


class AddPhotoToCollageHandler(CommandHandler[AddPhotoToCollage, None]):
    def __init__(
            self,
            photo_repo: PhotoRepo,
            collage_repo: CollageRepo,
            uow: UnitOfWork,
            mediator: EventMediator,
    ) -> None:
        self._photo_repo = photo_repo
        self._collage_repo = collage_repo
        self._uow = uow 
        self._mediator = mediator

    async def __call__(self, command: AddPhotoToCollage) -> None:
        photo = self._photo_repo.acquire_photo_by_id(PhotoId(command.photo_id))
        collage = self._collage_repo.get_collage_by_id(command.collage_id)

        collage.add_photo(photo.photo_id)
        photo.add_to_collage(command.collage_id,command.collage_url)

        await self._photo_repo.update_photo(photo)
        await self._collage_repo.update_collage(collage)

        events = photo.pull_events() + collage.pull_events()
        await self._mediator.publish(events)

        await self._uow.commit()

        logger.info("Photo added to collage", extra={"collage": collage})