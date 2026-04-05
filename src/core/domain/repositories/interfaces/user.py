from abc import abstractmethod

from core.domain.entities.user import User
from core.domain.repositories.interfaces.base import IBaseRepository


class IUserRepository(IBaseRepository):
    @abstractmethod
    def current(self) -> User:
        raise NotImplementedError

    @abstractmethod
    def all(
        self,
        records: int = 50,
        page: int = 0,
        order_by: str | None = None,
    ) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    def save(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def remove(self, user: User) -> User:
        raise NotImplementedError
