from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.sqlite.database import Base


class MaterialStorageModel(Base):
    __tablename__ = "material_storage"

    id: Mapped[UUID] = mapped_column(primary_key=True, unique=True, default=uuid4)
    quantity: Mapped[float] = mapped_column(nullable=False, default=0.0)

    material_id: Mapped[UUID] = mapped_column(ForeignKey("material.id"), nullable=False)
    warehouse_id: Mapped[UUID] = mapped_column(
        ForeignKey("warehouse.id"), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
