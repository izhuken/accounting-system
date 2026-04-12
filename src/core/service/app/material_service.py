from core.infrastructure.sqlite.repositories import MaterialRepository

from .base_entity_service import BaseEntityService


class MaterialService(BaseEntityService):
    def __init__(self) -> None:
        self._repository = MaterialRepository()
