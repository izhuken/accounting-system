from datetime import datetime

from core.domain.entities.entity import Entity
from core.domain.value_objects.size import SizeCode, SizeHeight


class Size(Entity):
    def __init__(
        self,
        code: SizeCode,
        height: SizeHeight,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._code = code
        self._height = height
        self._created_at = created_at
        self._updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Size):
            return self.code == obj.code
        return False

    @property
    def code(self) -> SizeCode:
        return self._code

    @property
    def height(self) -> SizeHeight:
        return self._height

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_height(self, height: SizeHeight) -> None:
        self._height = height
        self._updated_at = datetime.now()

    @staticmethod
    def create(code: SizeCode, height: SizeHeight) -> Size:
        return Size(
            code=code,
            height=height,
        )
