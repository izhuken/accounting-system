from abc import ABC, abstractmethod

from core.domain.dto import Paginated
from core.domain.entities.entity import Entity
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
    async def save(self, entity: Entity) -> Base:
        raise NotImplementedError

    @abstractmethod
    async def remove(self, entity: Entity) -> Base:
        raise NotImplementedError
