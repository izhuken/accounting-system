from core.domain.entities.user import User
from core.domain.value_objects.user import UserPassword
from core.infrastructure.sqlite.repositories import UserRepository
from core.service.exc import AuthenticationException

from .base_entity_service import BaseEntityService


class UserService(BaseEntityService):
    def __init__(self) -> None:
        self._repository = UserRepository()

    async def authenticate(self, password: str) -> User:
        user: User = await self._repository.current()

        if user.password == UserPassword(password):
            return user

        raise AuthenticationException

    async def current(self) -> User:
        return await self._repository.current()
