from typing import Any

from sqlalchemy import JSON, event
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


@event.listens_for(SessionEngine.sync_engine, "connect")
def set_sqlite_pragma(dbapi_connection, *args, **kwargs):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()


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
