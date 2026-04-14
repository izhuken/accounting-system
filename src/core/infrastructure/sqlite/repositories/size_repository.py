from math import ceil
from sqlite3 import IntegrityError as SQLiteIntegrityError

from sqlalchemy import delete, func, select
from sqlalchemy.exc import IntegrityError as SAIntegrityError

from core.domain.dto import Paginated
from core.domain.entities import Size
from core.domain.repositories.exc import FetchException
from core.domain.repositories.exc.remove import RemoveException
from core.domain.repositories.interfaces import ISizeRepository
from core.domain.value_objects.size import SizeCode
from core.infrastructure.sqlite.database import SessionLocal
from core.infrastructure.sqlite.models import SizeModel
from core.infrastructure.sqlite.repositories.base_repository import BaseRepository


class SizeRepository(BaseRepository, ISizeRepository):
    model = SizeModel

    async def all(
        self,
        records: int = 50,
        page: int = 0,
        order_by: str | None = None,
    ) -> Paginated[Size]:
        async with SessionLocal() as session:
            count_statement = select(func.count(self.model.code))
            statement = (
                select(self.model)
                .select_from(self.model)
                .offset(page * records)
                .limit(records)
            )
            statement = self._ordering_statement(statement, order_by)

            fetched_result = (await session.execute(statement)).scalars().unique().all()
            count_result = (await session.execute(count_statement)).scalar()

            if fetched_result is None:
                raise FetchException

            total_pages = ceil(count_result / records)

            return Paginated(
                data=[item.to_entity() for item in fetched_result],
                count=count_result,
                page=page,
                pages=total_pages,
                has_previous=page != 0,
                has_next=(page + 1) < total_pages,
            )

    async def one(self, code: SizeCode) -> Size:
        async with SessionLocal() as session:
            response = (
                await session.execute(
                    select(self.model)
                    .select_from(self.model)
                    .filter(self.model.code == code.value)
                )
            ).scalar_one_or_none()

            if not response:
                raise FetchException

            return response.to_entity()

    async def exists(self, entity: Size) -> bool:
        entity_model = self.model.from_entity(entity)

        async with SessionLocal() as session:
            response = (
                await session.execute(
                    select(self.model)
                    .select_from(self.model)
                    .filter(self.model.code == entity_model.code)
                )
            ).scalar_one_or_none()

            if not response:
                return False

            return True

    async def remove(self, entity: Size) -> Size:
        entity_model = self.model.from_entity(entity)

        async with SessionLocal.begin() as session:
            try:
                await session.execute(
                    delete(self.model).where(self.model.code == entity_model.code)
                )
                await session.commit()
            except SAIntegrityError, SQLiteIntegrityError:
                raise RemoveException

        return entity
