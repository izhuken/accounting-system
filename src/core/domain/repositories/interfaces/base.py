from abc import ABC, abstractmethod

from core.domain.dto import Paginated
from core.domain.entities.entity import Entity
from core.domain.value_objects.common.id_object import (
    UIntValueObjectId,
    UUIDValueObjectId,
)
from core.infrastructure.sqlite.database import Base


class IBaseRepository(ABC):
    model: Base

    @abstractmethod
    async def all(
        self,
        records: int = 50,
        page: int = 0,
        order_by: str | None = None,
    ) -> Paginated[Entity]:
        raise NotImplementedError

    @abstractmethod
    async def one(self, _id: UIntValueObjectId | UUIDValueObjectId) -> Entity:
        raise NotImplementedError

    @abstractmethod
    async def exists(self, entity: Entity) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def save(self, entity: Entity) -> Base:
        raise NotImplementedError

    @abstractmethod
    async def remove(self, entity: Entity) -> Base:
        raise NotImplementedError
