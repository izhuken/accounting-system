from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.sqlite.database import Base


class ContractorModel(Base):
    __tablename__ = "contractors"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, unique=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    email: Mapped[str] = mapped_column(String(256), nullable=True, default=None)
    phone: Mapped[str] = mapped_column(String(32), nullable=True, default=None)

    # address
    city: Mapped[str] = mapped_column(String(64), nullable=False)
    street: Mapped[str] = mapped_column(String(64), nullable=True, default=None)
    house: Mapped[str] = mapped_column(String(32), nullable=True, default=None)
    building: Mapped[str] = mapped_column(String(32), nullable=True, default=None)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
