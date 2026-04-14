from datetime import datetime

from core.domain.entities.entity import Entity
from core.domain.value_objects.color.color_id import ColorId
from core.domain.value_objects.color.color_name import ColorName


class Color(Entity):
    def __init__(
        self,
        id: ColorId,
        name: str,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._id = id
        self._name = ColorName(name)
        self._created_at = created_at
        self._updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Color):
            return self.id == obj.id

        return False

    @property
    def id(self) -> ColorId:
        return self._id

    @property
    def name(self) -> ColorName:
        return self._name

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: str) -> None:
        self._name = ColorName(name)
        self._updated_at = datetime.now()

    @staticmethod
    def create(name: str) -> Color:
        return Color(
            id=ColorId.generate(),
            name=name,
        )
