from datetime import datetime

from core.domain.value_objects.warehouse import (
    WarehouseAddress,
    WarehouseId,
    WarehouseName,
)


class Warehouse:
    def __init__(
        self,
        id: WarehouseId,
        name: WarehouseName,
        address: WarehouseAddress = None,
        created_ad: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._id = id
        self._name = name
        self._address = address
        self._created_ad = created_ad
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
        return self._created_ad

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: WarehouseName) -> None:
        self._name = name
        self._updated_at = datetime.now()

    def update_address(self, address: WarehouseAddress) -> None:
        self._address = address
        self._updated_at = datetime.now()

    @staticmethod
    def create(name: WarehouseName, address: WarehouseAddress) -> Warehouse:
        return Warehouse(
            id=WarehouseId.generate(),
            name=name,
            address=address,
        )
