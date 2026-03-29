from dataclasses import dataclass
from hashlib import sha256
from re import search

from core.domain.value_objects.common import ValueObject


@dataclass(frozen=True)
class UserPassword(ValueObject):
    value: str

    def __post_init__(self) -> None:
        self.__validate_length()
        self.value = self.__get_password_hash(self.value)

    def __str__(self) -> str:
        return self.value

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, UserPassword):
            return self.value == obj.value

        return False

    def __validate_length(self) -> None:
        if not self.value:
            raise ValueError("Имя не может быть пустым!")

        if len(self.value) < 6:
            raise ValueError("Размер имени не может быть меньше 6 символов!")

        if len(self.value) > 128:
            raise ValueError("Размер имени не может превышать 128 символов!")

        # проверка на наличие зашлавных символов
        if not search(r"[A-Z]", self.value):
            raise ValueError("Пароль должен содержать заглавные буквы")

        # проверка на наличие строчных символов
        if not search(r"[a-z]", self.value):
            raise ValueError("Пароль должен содержать строчные буквы")

        # проверка на наличие цифр
        if not search(r"[0-9]", self.value):
            raise ValueError("Пароль должен содержать цифры")

        # проверка на наличие спецсимволов
        if not search(r"[@$!%*#?&]", self.value):
            raise ValueError("Пароль должен содержать спецсимволы")

    def __get_password_hash(self, password: str) -> str:
        hash_object = sha256(password.encode())
        return hash_object.hexdigest()
