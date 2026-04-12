from sqlalchemy import select

from core.domain.entities.user import User
from core.domain.repositories.exc import FetchException
from core.domain.repositories.interfaces import IUserRepository
from core.domain.value_objects.user import UserStatus
from core.infrastructure.sqlite.database import Base, SessionLocal
from core.infrastructure.sqlite.models import UserModel
from core.infrastructure.sqlite.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository, IUserRepository):
    model: Base = UserModel

    async def current(self) -> User:
        async with SessionLocal() as session:
            response: UserModel | None = (
                await session.execute(
                    select(UserModel)
                    .select_from(UserModel)
                    .filter(UserModel.status == UserStatus.LOGGED_IN)
                )
            ).scalar_one_or_none()

            if not response:
                raise FetchException

            return response.to_entity()
