from datetime import datetime
from typing import Any

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.sqlite.database import Base


class InvoiceSnapshotModel(Base):
    __tablename__ = "invoice_snapshots"

    snapshot: Mapped[list[Any]] = mapped_column(default=[], nullable=False)

    invoice_id: Mapped[int] = mapped_column(ForeignKey("order.id"), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
