from enum import Enum

from core.domain.value_objects.common import ValueObject


class InvoiceType(ValueObject, Enum):
    INCOMING = "incoming"
    TRANSFER = "transfer"
    OUTGOING = "outgoing"
