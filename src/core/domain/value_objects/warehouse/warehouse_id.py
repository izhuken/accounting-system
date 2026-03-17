from dataclasses import dataclass
from uuid import UUID, uuid4

from core.domain.value_objects.common import UUIDValueObjectId


@dataclass(frozen=True)
class WarehouseId(UUIDValueObjectId):
    value: UUID

    @staticmethod
    def generate() -> WarehouseId:
        return WarehouseId(uuid4())
