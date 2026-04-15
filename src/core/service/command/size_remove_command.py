from core.domain.value_objects.size import SizeCode
from core.service.app import SizeService

from .base_commands import BaseRemoveCommand


class SizeRemoveCommand(BaseRemoveCommand):
    service = SizeService

    async def execute(self, code: int) -> None:
        service = self.service()
        entity = await service.one(SizeCode(code))
        await service.remove(entity)
