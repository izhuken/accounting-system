from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.domain.entities.invoice import Invoice
from core.domain.value_objects.invoice import InvoiceId, InvoiceType
from core.domain.value_objects.invoice.invoice_person import InvoicePerson
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

    def to_entity(self) -> Invoice:
        return Invoice(
            id=InvoiceId(self.id),
            type=InvoiceType(self.type),
            is_approved=self.is_approved,
            sender_person=InvoicePerson(self.sender_person),
            recipient_person=InvoicePerson(self.recipient_person),
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(entity: Invoice) -> InvoiceModel:
        return InvoiceModel(
            id=entity.id.value,
            type=entity.type.value,
            is_approved=entity.is_approved,
            sender_person=entity.sender_person.value,
            recipient_person=entity.recipient_person.value,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
