from core.domain.entities import Size
from core.domain.value_objects.size import SizeCode
from core.infrastructure.sqlite.repositories import SizeRepository

from .base_entity_service import BaseEntityService


class SizeService(BaseEntityService):
    def __init__(self) -> None:
        self._repository = SizeRepository()

    async def one(self, code: SizeCode) -> Size:
        return await self._repository.one(code)
