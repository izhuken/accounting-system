from math import ceil
from sqlite3 import IntegrityError as SQLiteIntegrityError

from sqlalchemy import Select, delete, func, select
from sqlalchemy.exc import IntegrityError as SAIntegrityError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

from core.domain.dto import Paginated
from core.domain.entities.entity import Entity
from core.domain.repositories.exc import FetchException, RemoveException, SaveException
from core.domain.repositories.interfaces import IBaseRepository
from core.domain.value_objects.common.id_object import (
    UIntValueObjectId,
    UUIDValueObjectId,
)
from core.infrastructure.sqlite.database import Base, SessionLocal


class BaseRepository(IBaseRepository):
    model: Base
    additional_fields: list[str] = []

    async def all(
        self,
        records: int = 50,
        page: int = 0,
        order_by: str | None = None,
    ) -> Paginated[Entity]:
        async with SessionLocal() as session:
            count_statement = select(func.count(self.model.id))
            statement = (
                select(self.model)
                .select_from(self.model)
                .offset(page * records)
                .limit(records)
            )
            statement = self._ordering_statement(statement, order_by)
            statement = self._select_additional_fields(statement)

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

    async def one(self, _id: UUIDValueObjectId | UIntValueObjectId) -> Entity:
        statement = (
            select(self.model)
            .select_from(self.model)
            .filter(self.model.id == _id.value)
        )
        statement = self._select_additional_fields(statement)

        async with SessionLocal() as session:
            response = (await session.execute(statement)).scalar_one_or_none()

            if not response:
                raise FetchException

            return response.to_entity()

    async def exists(self, entity: Entity) -> bool:
        entity_model = self.model.from_entity(entity)

        async with SessionLocal() as session:
            response = (
                await session.execute(
                    select(self.model)
                    .select_from(self.model)
                    .filter(self.model.id == entity_model.id)
                )
            ).scalar_one_or_none()

            if not response:
                return False

            return True

    async def save(self, entity: Entity) -> Entity:
        entity_model = self.model.from_entity(entity)

        async with SessionLocal.begin() as session:
            try:
                merged_model: Base = await session.merge(entity_model)
                await session.flush()
                await session.refresh(
                    merged_model,
                    attribute_names=self.additional_fields,
                )
                return merged_model.to_entity()
            except SQLAlchemyError:
                raise SaveException

    async def remove(self, entity: Entity) -> Entity:
        entity_model = self.model.from_entity(entity)

        async with SessionLocal.begin() as session:
            try:
                await session.execute(
                    delete(self.model).where(self.model.id == entity_model.id)
                )
                await session.commit()
            except SAIntegrityError, SQLiteIntegrityError:
                raise RemoveException

        return entity

    def _ordering_statement(
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

    def _select_additional_fields(self, statement: Select) -> Select:
        for _field in self.additional_fields:
            statement = statement.options(selectinload(getattr(self.model, _field)))

        return statement
