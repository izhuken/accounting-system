from re import Match

from .value_object import ValueObject


class EmailValueObject(ValueObject):
    value: str

    def __post__init__(self) -> None:
        self.__validate()

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, type(self)):
            return self.value == obj.value

        return False

    def __validate(self) -> None:
        if len(self.value) == 0:
            raise ValueError("E-mail не может быть пустым!")

        if not Match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.value):
            raise ValueError("E-mail не соответствует формату!")
