from abc import ABC, abstractmethod

from core.domain.dto.paginated import Paginated
from core.domain.entities.entity import Entity


class IEntityService(ABC):
    @abstractmethod
    async def all(self) -> Paginated[Entity]:
        raise NotImplementedError

    @abstractmethod
    async def one(self, _id: str) -> Entity:
        raise NotImplementedError

    @abstractmethod
    async def exists(self, entity: Entity) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def save(self, entity: Entity) -> Entity:
        raise NotImplementedError

    @abstractmethod
    async def remove(self, entity: Entity) -> Entity:
        raise NotImplementedError
