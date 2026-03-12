from uuid import UUID


class UUIDValueObjectId:
    value: UUID

    @staticmethod
    def generate() -> UUIDValueObjectId:
        pass

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, type(self)):
            return self.value == obj.value

        return False


class UIntValueObjectId:
    value: int

    @staticmethod
    def generate(id: int) -> UIntValueObjectId:
        pass

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, type(self)):
            return self.value == obj.value

        return False
