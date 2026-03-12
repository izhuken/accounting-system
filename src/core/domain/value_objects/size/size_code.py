from dataclasses import dataclass

from core.domain.value_objects.common import ValueObject


@dataclass(frozen=True)
class SizeCode(ValueObject):
    value: str

    def __str__(self) -> str:
        return self.value

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, SizeCode):
            return self.value == obj.value

        return False
