from dataclasses import dataclass

from core.domain.value_objects.common import ValueObject


@dataclass(frozen=True)
class InvoicePerson(ValueObject):
    value: str

    def __post_init__(self) -> None:
        self.__validate()

    def __str__(self) -> str:
        return self.value

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, InvoicePerson):
            return self.value == obj.value

        return False

    def __validate(self) -> None:
        if not self.value:
            raise ValueError("Имя не может быть пустым!")

        if len(self.value) > 256:
            raise ValueError("Размер имени не может превышать 512 символов!")
