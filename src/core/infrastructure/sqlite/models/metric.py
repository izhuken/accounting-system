from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.infrastructure.sqlite.database import Base


class MetricModel(Base):
    __tablename__ = "metrics"

    code: Mapped[int] = mapped_column(
        Integer(), nullable=False, unique=True, primary_key=True
    )
    name: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
