from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.sqlite.database import Base


class SizeModel(Base):
    __tablename__ = "sizes"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, unique=True)
    code: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    height: Mapped[str] = mapped_column(String(32), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
