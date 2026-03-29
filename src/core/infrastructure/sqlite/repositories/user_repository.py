from sqlalchemy import delete, select

from core.domain.entities.user import User
from core.domain.repositories import IUserRepository
from core.domain.value_objects.user import UserStatus
from core.infrastructure.sqlite.database import SessionLocal
from core.infrastructure.sqlite.models import UserModel


class UserRepository(IUserRepository):
    def current(self) -> User:
        with SessionLocal() as session:
            response: UserModel | None = session.execute(
                select(UserModel)
                .select_from(UserModel)
                .filter(UserModel.status == UserStatus.LOGGED_IN)
            ).first()

            if not response:
                raise ...

            return response.to_entity()

    def all(
        self,
        records: int = 50,
        page: int = 0,
        order_by: str | None = None,
    ) -> list[User]:
        raise NotImplementedError

    def save(self, user: User) -> User:
        raise NotImplementedError

    def remove(self, user: User) -> User:
        with SessionLocal.session() as session:
            session.execute(delete(UserModel).where(UserModel.id == user.id))
            session.commit()
        return user
