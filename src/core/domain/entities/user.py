from datetime import datetime

from core.domain.entities.entity import Entity
from core.domain.value_objects.user import UserId, UserName, UserPassword, UserStatus


class User(Entity):
    def __init__(
        self,
        id: UserId,
        username: UserName,
        password: UserPassword,
        status: UserStatus = UserStatus.INACTIVE,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._id = id
        self._username = username
        self._password = password
        self._status = status
        self._created_at = created_at
        self._updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, User):
            return self.id == obj.id

        return False

    @property
    def id(self) -> UserId:
        return self._id

    @property
    def username(self) -> UserName:
        return self._username

    @property
    def password(self) -> UserPassword:
        return self._password

    @property
    def status(self) -> UserStatus:
        return self._status

    @property
    def is_active(self) -> bool:
        return self._status == UserStatus.LOGGED_IN

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_username(self, username: UserName) -> None:
        self._username = username
        self._updated_at = datetime.now()

    def update_password(self, password: UserPassword) -> None:
        self._password = password
        self._updated_at = datetime.now()

    def login(self, username: UserName, password: UserPassword) -> bool:
        if self._username == username and self._password == password:
            self._status = UserStatus.LOGGED_IN
            return True

        return False

    @staticmethod
    def create(username: UserName, password: UserPassword) -> User:
        return User(
            id=UserId.generate(),
            username=username,
            password=password,
        )
