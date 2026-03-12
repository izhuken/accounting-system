from dataclasses import dataclass

from core.domain.value_objects.common import UIntValueObjectId


@dataclass(frozen=True)
class InvoiceId(UIntValueObjectId):
    value: int

    @staticmethod
    def generate(value: int) -> InvoiceId:
        return InvoiceId(value)
