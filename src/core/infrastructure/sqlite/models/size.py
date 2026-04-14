from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.domain.entities.size import Size
from core.infrastructure.sqlite.database import Base


class SizeModel(Base):
    __tablename__ = "sizes"

    code: Mapped[str] = mapped_column(
        String(32), nullable=False, unique=True, primary_key=True
    )
    height: Mapped[str] = mapped_column(String(32), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def to_entity(self) -> Size:
        return Size(
            id=self.code,
            height=self.height,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(entity: Size) -> SizeModel:
        return SizeModel(
            code=entity.id.value,
            height=entity.height.value,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
