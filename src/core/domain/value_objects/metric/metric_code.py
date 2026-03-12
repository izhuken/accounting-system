from dataclasses import dataclass

from core.domain.value_objects.common import ValueObject


@dataclass(frozen=True)
class MetricCode(ValueObject):
    value: int

    def __post_init__(self) -> None:
        self.__validate()

    def __int__(self) -> int:
        return self.value

    def __float__(self) -> float:
        return float(self.value)

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, MetricCode):
            return self.value == obj.value

        return False

    def __validate(self) -> None:
        if not self.value:
            raise ValueError("Код метрики не может быть пустым!")

        if self.value < 0:
            raise ValueError("Код метрики не может быть отрицательным числом!")

        if self.value > 9999:
            raise ValueError("Код метрики не может быть больше 9999!")
