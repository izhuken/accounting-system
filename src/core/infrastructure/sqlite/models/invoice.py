from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.domain.value_objects.invoice import InvoiceType
from core.infrastructure.sqlite.database import Base


class InvoiceModel(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    type: Mapped[str] = mapped_column(
        Enum(InvoiceType), nullable=False, default=InvoiceType.INCOMING
    )
    is_approved: Mapped[bool] = mapped_column(nullable=False, default=False)
    sender_person: Mapped[str] = mapped_column(String(256), nullable=True, default=None)
    recipient_person: Mapped[str] = mapped_column(
        String(256), nullable=True, default=None
    )

    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), nullable=True)
    sender_warehouse_id: Mapped[UUID] = mapped_column(
        ForeignKey("warehouse.id"), nullable=True, default=None
    )
    recipient_warehouse_id: Mapped[UUID] = mapped_column(
        ForeignKey("warehouse.id"), nullable=True, default=None
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
