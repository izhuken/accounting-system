from typing import Any

from sqlalchemy import JSON, Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from core.config import Config
from core.domain.entities.entity import Entity

SessionEngine: Engine = create_engine(Config.db_url)

SessionLocal: sessionmaker[Session] = sessionmaker(bind=SessionEngine, autoflush=True)


class Base(DeclarativeBase):
    type_annotation_map = {list[Any]: JSON}

    def to_entity(self) -> Entity:
        raise NotImplementedError

    @staticmethod
    def from_entity(entity: Entity) -> Base:
        raise NotImplementedError
