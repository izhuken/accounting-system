from dataclasses import dataclass

from core.domain.value_objects.common import UIntValueObjectId


@dataclass(frozen=True)
class OrderId(UIntValueObjectId):
    value: int

    @staticmethod
    def generate(value: int) -> OrderId:
        return OrderId(value)
