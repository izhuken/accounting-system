from sqlalchemy import Select, delete, func, select
from sqlalchemy.exc import SQLAlchemyError

from core.domain.dto import Paginated
from core.domain.entities.user import User
from core.domain.repositories.exc import FetchException, SaveException
from core.domain.repositories.interfaces import IUserRepository
from core.domain.value_objects.user import UserStatus
from core.infrastructure.sqlite.database import Base, SessionLocal
from core.infrastructure.sqlite.models import UserModel


class UserRepository(IUserRepository):
    model: Base = UserModel

    def current(self) -> User:
        with SessionLocal() as session:
            response: UserModel | None = session.execute(
                select(UserModel)
                .select_from(UserModel)
                .filter(UserModel.status == UserStatus.LOGGED_IN)
            ).scalar_one_or_none()

            if not response:
                raise FetchException

            return response.to_entity()

    def all(
        self,
        records: int = 50,
        page: int = 0,
        order_by: str | None = None,
    ) -> Paginated[User]:
        with SessionLocal() as session:
            count_statement = select(func.count(self.model.id))
            statement = (
                select(self.model)
                .select_from(self.model)
                .offset((page - 1) * records)
                .limit(records)
            )
            statement = self.__ordering_statement(statement, order_by)

            fetched_result = session.execute(statement).scalars().unique().all()
            count_result = session.execute(count_statement).scalar()

            if not fetched_result:
                raise FetchException

            return Paginated(
                items=[item.to_entity() for item in fetched_result],
                count=count_result,
                page=page,
                has_previous=(page > 1),
                has_next=(count_result > page * records),
            )

    def exists(self, entity: User) -> bool:
        entity_model = self.model.from_entity(entity)

        with SessionLocal() as session:
            response = session.execute(
                select(self.model)
                .select_from(self.model)
                .filter(self.model.id == entity_model.id)
            ).scalar_one_or_none()

            if not response:
                return False

            return True

    def save(self, entity: User) -> User:
        entity_model = self.model.from_entity(entity)

        with SessionLocal() as session:
            try:
                merged_model = session.merge(entity_model)
                session.commit()
                return merged_model.to_entity()
            except SQLAlchemyError:
                session.rollback()
                raise SaveException

    def remove(self, entity: User) -> User:
        entity_model = self.model.from_entity(entity)

        with SessionLocal() as session:
            session.execute(delete(self.model).where(self.model.id == entity_model.id))
            session.commit()

        return entity

    def __ordering_statement(
        self, statement: Select, order_column: str | None = None
    ) -> Select:
        reverse = False

        if order_column is None:
            return statement

        if order_column.startswith("-"):
            reverse = True
            order_column = order_column[1:]

        if not hasattr(self.model, order_column):
            return statement

        attribute = getattr(self.model, order_column)
        return statement.order_by(attribute.desc() if reverse else attribute.asc())
