from core.domain.entities import Metric
from core.domain.value_objects.metric import MetricCode
from core.infrastructure.sqlite.repositories import MetricRepository

from .base_entity_service import BaseEntityService


class MetricService(BaseEntityService):
    def __init__(self) -> None:
        self._repository = MetricRepository()

    async def one(self, code: MetricCode) -> Metric:
        return await self._repository.one(code)
