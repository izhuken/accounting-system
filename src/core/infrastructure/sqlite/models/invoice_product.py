from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.sqlite.database import Base


class InvoiceProductModel(Base):
    __tablename__ = "invoice_products"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, unique=True)
    quantity: Mapped[float] = mapped_column(nullable=False, default=0.0)

    product_id: Mapped[UUID] = mapped_column(ForeignKey("product.id"), nullable=False)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("order.id"), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
