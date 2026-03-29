from core.domain.entities.user import User
from core.domain.repositories import IUserRepository
from core.domain.value_objects.user import UserPassword


class UserService:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    def authenticate(self, password: str) -> User:
        user: User = self._repository.current()

        if user.password != UserPassword(password):
            raise

        return user

    def fetch_current(self) -> User:
        return self._repository.current()
