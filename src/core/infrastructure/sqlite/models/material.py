from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.domain.entities.material import Material
from core.domain.value_objects.material import MaterialId
from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.fields import EncryptedString


class MaterialModel(Base):
    __tablename__ = "materials"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, unique=True)
    name: Mapped[str] = mapped_column(EncryptedString, nullable=False, unique=True)

    # foreign keys
    metric_code: Mapped[int] = mapped_column(
        ForeignKey("metrics.code", ondelete="RESTRICT"), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    metric: Mapped["MetricModel"] = relationship(backref="materials")

    def to_entity(self) -> Material:
        return Material(
            id=MaterialId(self.id),
            name=self.name,
            metric=self.metric.to_entity(),
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(entity: Material) -> MaterialModel:
        return MaterialModel(
            id=entity.id.value,
            name=entity.name.value,
            metric_code=entity.metric.code.value,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
