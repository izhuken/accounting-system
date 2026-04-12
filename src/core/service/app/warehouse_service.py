from core.infrastructure.sqlite.repositories import WarehouseRepository

from .base_entity_service import BaseEntityService


class WarehouseService(BaseEntityService):
    def __init__(self) -> None:
        self._repository = WarehouseRepository()
