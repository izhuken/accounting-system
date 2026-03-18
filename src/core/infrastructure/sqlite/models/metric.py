from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.domain.entities.metric_code import Metric
from core.domain.value_objects.metric.metric_code import MetricCode
from core.domain.value_objects.metric.metric_name import MetricName
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

    def to_entity(self) -> Metric:
        return Metric(
            code=MetricCode(self.code),
            name=MetricName(self.name),
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(entity: Metric) -> MetricModel:
        return MetricModel(
            code=entity.code.value,
            name=entity.name.value,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
