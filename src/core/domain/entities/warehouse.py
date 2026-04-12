from datetime import datetime

from core.domain.entities.entity import Entity
from core.domain.value_objects.warehouse import (
    WarehouseAddress,
    WarehouseId,
    WarehouseName,
)


class Warehouse(Entity):
    def __init__(
        self,
        id: WarehouseId,
        name: str,
        address: WarehouseAddress,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._id = id
        self._name = WarehouseName(name)
        self._address = address
        self._created_at = created_at
        self._updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Warehouse):
            return False

        return self.id == obj.id

    @property
    def id(self) -> WarehouseId:
        return self._id

    @property
    def name(self) -> WarehouseName:
        return self._name

    @property
    def address(self) -> WarehouseAddress:
        return self._address

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: str) -> None:
        self._name = WarehouseName(name)
        self._updated_at = datetime.now()

    def update_address(self, address: WarehouseAddress) -> None:
        self._address = address
        self._updated_at = datetime.now()

    def to_dict(self) -> dict:
        return {
            "id": self.id.value,
            "name": self.name.value,
            "city": self.address.city,
            "street": self.address.street,
            "house": self.address.house,
            "building": self.address.building,
            "full_address": str(self.address),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(name: str, address: WarehouseAddress) -> Warehouse:
        return Warehouse(
            id=WarehouseId.generate(),
            name=name,
            address=address,
        )
