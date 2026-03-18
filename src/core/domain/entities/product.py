from datetime import datetime

from core.domain.entities.color import Color
from core.domain.entities.entity import Entity
from core.domain.entities.size import Size
from core.domain.value_objects.product import ProductId, ProductName


class Product(Entity):
    def __init__(
        self,
        id: ProductId,
        name: ProductName,
        size: Size,
        color: Color,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._id = id
        self._name = name
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
    def size(self) -> Size:
        return self._size

    @property
    def color(self) -> Color:
        return self._color

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: ProductName) -> None:
        self._name = name
        self._updated_at = datetime.now()

    def update_size(self, size: Size) -> None:
        self._size = size
        self._updated_at = datetime.now()

    def update_color(self, color: Color) -> None:
        self._color = color
        self._updated_at = datetime.now()

    @staticmethod
    def create(name: ProductName, size: Size, color: Color) -> Product:
        return Product(id=ProductId.generate(), name=name, size=size, color=color)
