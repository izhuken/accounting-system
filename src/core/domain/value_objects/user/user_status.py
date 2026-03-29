from enum import Enum

from core.domain.value_objects.common import ValueObject


class UserStatus(ValueObject, Enum):
    LOGGED_IN = "logged in"
    INACTIVE = "inactive"
