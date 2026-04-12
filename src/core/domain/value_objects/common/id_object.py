from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class UUIDValueObjectId:
    value: UUID

    @staticmethod
    def generate() -> UUIDValueObjectId:
        pass

    @staticmethod
    def create(_id: UUID) -> UUIDValueObjectId:
        return UUIDValueObjectId(_id)

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, type(self)):
            return self.value == obj.value

        return False


@dataclass(frozen=True)
class UIntValueObjectId:
    value: int

    @staticmethod
    def generate(id: int) -> UIntValueObjectId:
        pass

    @staticmethod
    def create(_id: int) -> UIntValueObjectId:
        return UIntValueObjectId(_id)

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, type(self)):
            return self.value == obj.value

        return False
