from core.domain.entities.user import User
from core.domain.value_objects.user.user_password import UserPassword
from core.infrastructure.sqlite.repositories import UserRepository
from core.service.exc import AuthenticationException


class UserService:
    def __init__(self) -> None:
        self._repository = UserRepository()

    async def authenticate(self, password: str) -> User:
        user: User = await self._repository.current()

        if user.password == UserPassword(password):
            return user

        raise AuthenticationException

    async def exists(self, user: User) -> bool:
        return await self._repository.exists(user)

    async def current(self) -> User:
        return await self._repository.current()

    async def save(self, user: User) -> User:
        return await self._repository.save(user)

    async def remove(self, user: User) -> User:
        return await self._repository.remove(user)
