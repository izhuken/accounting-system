from dataclasses import dataclass

from core.domain.value_objects.common import PhoneValueObject


@dataclass(frozen=True)
class ClientPhone(PhoneValueObject):
    value: str
