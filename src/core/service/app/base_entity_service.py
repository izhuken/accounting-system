from core.domain.dto import Paginated
from core.domain.entities.entity import Entity
from core.domain.repositories.interfaces.base import IBaseRepository
from core.domain.value_objects.common.id_object import (
    UIntValueObjectId,
    UUIDValueObjectId,
)

from .ientity_service import IEntityService


class BaseEntityService(IEntityService):
    def __init__(self) -> None:
        self._repository: IBaseRepository = None

    async def all(
        self, records: int = 50, page: int = 0, order_by: str | None = None
    ) -> Paginated[Entity]:
        return await self._repository.all(records=records, page=page, order_by=order_by)

    async def one(self, _id: UUIDValueObjectId | UIntValueObjectId) -> Entity:
        return await self._repository.one(_id)

    async def exists(self, entity: Entity) -> bool:
        return await self._repository.exists(entity)

    async def save(self, entity: Entity) -> Entity:
        return await self._repository.save(entity)

    async def remove(self, entity: Entity) -> Entity:
        return await self._repository.remove(entity)
