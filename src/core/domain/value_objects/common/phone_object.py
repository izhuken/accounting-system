from re import Match

from .value_object import ValueObject


class PhoneValueObject(ValueObject):
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
            raise ValueError("Телефон не может быть пустым!")

        patterns = (r"^\+7\d{10}$", r"^8\d{10}$", r"^7\d{10}$")

        for pattern, format_name in patterns.items():
            if Match(pattern, self.value):
                return

        raise ValueError("Телефон не соответствует формату!")
