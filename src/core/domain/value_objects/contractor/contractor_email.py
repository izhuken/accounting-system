from dataclasses import dataclass

from core.domain.value_objects.common import EmailValueObject


@dataclass(frozen=True)
class ContractorEmail(EmailValueObject):
    value: str
