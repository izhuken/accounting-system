from typing import Any

from sqlalchemy import JSON
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from core.config import Config
from core.domain.entities.entity import Entity

SessionEngine: AsyncEngine = create_async_engine(Config.db_url)

SessionLocal: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=SessionEngine, autoflush=True
)


class Base(DeclarativeBase):
    type_annotation_map = {list[Any]: JSON}

    def to_entity(self) -> Entity:
        raise NotImplementedError

    @staticmethod
    def from_entity(entity: Entity) -> Base:
        raise NotImplementedError
