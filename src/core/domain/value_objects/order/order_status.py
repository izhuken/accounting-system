from enum import Enum

from core.domain.value_objects.common import ValueObject


class OrderStatus(ValueObject, Enum):
    BACKLOG = "backlog"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
