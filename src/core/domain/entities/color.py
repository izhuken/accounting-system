from datetime import datetime

from core.domain.entities.entity import Entity
from core.domain.value_objects.color.color_id import ColorId
from core.domain.value_objects.color.color_name import ColorName


class Color(Entity):
    def __init__(
        self,
        id: ColorId,
        name: ColorName,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._id = id
        self._name = name
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

    def update_name(self, name: ColorName) -> None:
        self._name = name
        self._updated_at = datetime.now()

    @staticmethod
    def create(name: ColorName) -> Color:
        return Color(
            id=ColorId.generate(),
            name=name,
        )
