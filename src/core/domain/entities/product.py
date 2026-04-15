from datetime import datetime

from core.domain.entities.color import Color
from core.domain.entities.entity import Entity
from core.domain.entities.size import Size
from core.domain.value_objects.product import ProductId, ProductName


class Product(Entity):
    def __init__(
        self,
        id: ProductId,
        name: str,
        size: Size | None = None,
        color: Color | None = None,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._id = id
        self._name = ProductName(name)
        self._size = size
        self._color = color
        self._created_at = created_at
        self._updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Product):
            return self.id == obj.id

        return False

    @property
    def id(self) -> ProductId:
        return self._id

    @property
    def name(self) -> ProductName:
        return self._name

    @property
    def size(self) -> Size | None:
        return self._size

    @property
    def color(self) -> Color | None:
        return self._color

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: str) -> None:
        self._name = ProductName(name)
        self._updated_at = datetime.now()

    def update_size(self, size: Size | None = None) -> None:
        self._size = size
        self._updated_at = datetime.now()

    def update_color(self, color: Color | None = None) -> None:
        self._color = color
        self._updated_at = datetime.now()

    def to_dict(self) -> dict:
        return {
            "id": self.id.value,
            "name": self.name.value,
            "size": self.size.to_dict() if self.size else None,
            "color": self.color.to_dict() if self.color else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(
        name: str, size: Size | None = None, color: Color | None = None
    ) -> Product:
        return Product(id=ProductId.generate(), name=name, size=size, color=color)
