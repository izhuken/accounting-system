from dataclasses import dataclass
from uuid import UUID, uuid4

from core.domain.value_objects.common import UUIDValueObjectId


@dataclass(frozen=True)
class StockId(UUIDValueObjectId):
    value: UUID

    @staticmethod
    def generate() -> StockId:
        return StockId(uuid4())
