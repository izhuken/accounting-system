from datetime import datetime

from core.domain.entities.entity import Entity
from core.domain.value_objects.order import OrderId, OrderStatus

from .client import Client
from .contractor import Contractor
from .warehouse import Warehouse


class Order(Entity):
    def __init__(
        self,
        id: OrderId,
        status: OrderStatus,
        client: Client,
        contractor: Contractor,
        base_warehouse: Warehouse,
        contractor_warehouse: Warehouse,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._id = id
        self._status = status
        self._client = client
        self._contractor = contractor
        self._base_warehouse = base_warehouse
        self._contractor_warehouse = contractor_warehouse
        self._created_at = created_at
        self._updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Order):
            return self.id == obj.id

        return False

    @property
    def id(self) -> OrderId:
        return self._id

    @property
    def status(self) -> OrderStatus:
        return self._status

    @property
    def client(self) -> Client:
        return self._client

    @property
    def contractor(self) -> Contractor:
        return self._contractor

    @property
    def base_warehouse(self) -> Warehouse:
        return self._base_warehouse

    @property
    def contractor_warehouse(self) -> Warehouse:
        return self._contractor_warehouse

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    @property
    def is_backlog(self) -> bool:
        return self._status == OrderStatus.BACKLOG

    @property
    def is_in_progress(self) -> bool:
        return self._status == OrderStatus.IN_PROGRESS

    @property
    def is_completed(self) -> bool:
        return self._status == OrderStatus.COMPLETED

    @property
    def is_cancelled(self) -> bool:
        return self._status == OrderStatus.CANCELLED

    @property
    def is_closed(self) -> bool:
        return self.is_completed or self.is_cancelled

    def update_status(self, status: OrderStatus) -> None:
        self._status = status
        self._updated_at = datetime.now()

    def update_client(self, client: Client) -> None:
        self._client = client
        self._updated_at = datetime.now()

    def update_contractor(self, contractor: Contractor) -> None:
        self._contractor = contractor
        self._updated_at = datetime.now()

    def update_base_warehouse(self, base_warehouse: Warehouse) -> None:
        self._base_warehouse = base_warehouse
        self._updated_at = datetime.now()

    def update_contractor_warehouse(self, contractor_warehouse: Warehouse) -> None:
        self._contractor_warehouse = contractor_warehouse
        self._updated_at = datetime.now()

    @staticmethod
    def create(
        self,
        id: OrderId,
        status: OrderStatus,
        client: Client,
        contractor: Contractor,
        base_warehouse: Warehouse,
        contractor_warehouse: Warehouse,
    ) -> Order:
        return Order(
            id=id,
            status=status,
            client=client,
            contractor=contractor,
            base_warehouse=base_warehouse,
            contractor_warehouse=contractor_warehouse,
        )
