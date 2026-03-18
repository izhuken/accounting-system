from enum import Enum

from core.domain.value_objects.common import ValueObject


class InvoiceStatus(ValueObject, Enum):
    NEW = "NEW"
    APPROVED = "APPROVED"
    REAPPROVED = "REAPPROVED"
