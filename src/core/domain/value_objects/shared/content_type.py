from enum import Enum

from core.domain.value_objects.common import ValueObject


class ContentType(ValueObject, Enum):
    PRODUCT = "product"
    MATERIAL = "material"
