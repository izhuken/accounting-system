from abc import abstractmethod

from core.domain.entities.user import User
from core.domain.repositories.interfaces.base import IBaseRepository


class IUserRepository(IBaseRepository):
    @abstractmethod
    async def current(self) -> User:
        raise NotImplementedError

    @abstractmethod
    async def all(
        self,
        records: int = 50,
        page: int = 0,
        order_by: str | None = None,
    ) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    async def save(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    async def remove(self, user: User) -> User:
        raise NotImplementedError
