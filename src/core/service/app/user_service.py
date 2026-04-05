from core.domain.entities.user import User
from core.domain.value_objects.user.user_password import UserPassword
from core.infrastructure.sqlite.repositories import UserRepository
from core.service.exc import AuthenticationException


class UserService:
    def __init__(self) -> None:
        self._repository = UserRepository()

    def authenticate(self, password: str) -> User:
        user: User = self._repository.current()

        if user.password == UserPassword(password):
            return user

        raise AuthenticationException

    def exists(self, user: User) -> bool:
        return self._repository.exists(user)

    def current(self) -> User:
        return self._repository.current()

    def save(self, user: User) -> User:
        return self._repository.save(user)

    def remove(self, user: User) -> User:
        return self._repository.remove(user)
