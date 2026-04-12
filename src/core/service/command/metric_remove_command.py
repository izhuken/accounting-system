from core.domain.value_objects.metric import MetricCode
from core.service.app import MetricService

from .base_commands import BaseRemoveCommand


class MetricRemoveCommand(BaseRemoveCommand):
    service = MetricService

    async def execute(self, code: int) -> None:
        service = self.service()
        entity = await service.one(MetricCode(code))
        await service.remove(entity)
