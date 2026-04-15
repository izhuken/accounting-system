from core.infrastructure.sqlite.repositories import ProductRepository

from .base_entity_service import BaseEntityService


class ProductService(BaseEntityService):
    def __init__(self) -> None:
        self._repository = ProductRepository()
