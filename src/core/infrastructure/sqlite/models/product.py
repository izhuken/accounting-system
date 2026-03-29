from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.fields import EncryptedString


class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, unique=True)
    name: Mapped[str] = mapped_column(EncryptedString, nullable=False, unique=True)

    # foreign keys
    size_id: Mapped[UUID] = mapped_column(ForeignKey("sizes.code"), nullable=False)
    color_id: Mapped[UUID] = mapped_column(ForeignKey("colors.id"), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
