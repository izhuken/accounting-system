from dataclasses import dataclass

from core.domain.value_objects.common import EmailValueObject


@dataclass(frozen=True)
class ClientEmail(EmailValueObject):
    value: str
