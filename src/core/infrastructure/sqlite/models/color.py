from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.domain.entities.color import Color
from core.infrastructure.sqlite.database import Base


class ColorModel(Base):
    __tablename__ = "colors"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, unique=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def to_entity(self) -> Color:
        return Color(id=self.id, name=self.name)

    @staticmethod
    def from_entity(entity: Color) -> ColorModel:
        return ColorModel(id=entity.id.value, name=entity.name.value)
