import logging 
from dataclasses import dataclass
from uuid import UUID, uuid4 

from didiator import EventMediator
from src.application.common.command import Command, CommandHandler
from src.application.common.interfaces.uow import UnitOfWork
from src.application.photo.interfaces import PhotoRepo
from src.domain.mirror_support.category.value_objects.category_id import CategoryId
from src.domain.mirror_core.photo.entities import Photo
from src.domain.mirror_core.photo.value_objects import PhotoDescription,PhotoId,PhotoUrl, DeletionTime


logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class AddPhoto(Command[UUID]):    
    photo_description: str 
    category_id: UUID 
    telegram_file_id: str | None = None 
    photo_url: str | None = None
    


class AddPhotoHandler(CommandHandler[AddPhoto, UUID]):
    def __init__(self, photo_repo: PhotoRepo, uow: UnitOfWork, mediator: EventMediator):
        self._photo_repo = photo_repo
        #self._category_repo = category_repo
        self._uow = uow 
        self._mediator = mediator
    
    async def __call__(self, command: AddPhoto) -> UUID:
        photo_id = PhotoId(uuid4())
        photo_url = PhotoUrl(command.photo_url)
        photo_description = PhotoDescription(command.photo_description)
        category_id = CategoryId(command.category_id)

        # if not await self._category_repo.exists(category_id):
        #     raise CategoryDoesNotExistError(category_id.to_raw())
        
        photo = Photo.create(photo_id, photo_url, photo_description, category_id)
        await self._photo_repo.add_photo(photo)
        await self._mediator.publish(photo.pull_events())
        await self._uow.commit()

        logger.info("Photo Created", extra={"photo": photo})

        return photo_id.to_raw()