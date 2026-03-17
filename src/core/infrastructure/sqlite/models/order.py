from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from core.domain.value_objects.order import OrderStatus
from core.infrastructure.sqlite.database import Base


class OrderModel(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus), nullable=False, default=OrderStatus.NEW
    )

    base_warehouse_id: Mapped[UUID] = mapped_column(
        ForeignKey("warehouse.id"), nullable=True, default=None
    )
    contractor_warehouse_id: Mapped[UUID] = mapped_column(
        ForeignKey("warehouse.id"), nullable=True, default=None
    )
    contractor_id: Mapped[UUID] = mapped_column(
        ForeignKey("contractor.id"), nullable=True, default=None
    )
    client_id: Mapped[UUID] = mapped_column(
        ForeignKey("client.id"), nullable=True, default=None
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
