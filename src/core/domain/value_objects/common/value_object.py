from typing import Any


class ValueObject:
    value: Any

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, type(self)):
            return self.value == obj.value

        return False

    def __hash__(self) -> int:
        return hash(self.value)
