from uuid import UUID

from core.domain.value_objects.common.id_object import UUIDValueObjectId
from core.service.app.ientity_service import IEntityService

from .icommand import ICommand


class BaseRemoveCommand(ICommand):
    service: IEntityService

    async def execute(self, _id: int | UUID) -> None:
        if isinstance(_id, UUID):
            id_object = UUIDValueObjectId.create(_id)
        else:
            id_object = UUIDValueObjectId.create(str(_id))

        service = self.service()
        entity = await service.one(id_object)
        await service.remove(entity)
