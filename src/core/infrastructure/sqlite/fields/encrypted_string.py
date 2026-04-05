from cryptography.fernet import Fernet
from sqlalchemy import Dialect
from sqlalchemy.types import LargeBinary, TypeDecorator

from core.config import Config


class EncryptedString(TypeDecorator):
    impl = LargeBinary
    _cipher = Fernet(Config.secret_key)

    def process_bind_param(self, value: str, dialect: Dialect) -> bytes:
        if value is None:
            return value
        return self._cipher.encrypt(value.encode())

    def process_result_value(self, value: str, dialect: Dialect) -> str:
        if value is None:
            return value
        return self._cipher.decrypt(value).decode()
