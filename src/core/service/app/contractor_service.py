from core.infrastructure.sqlite.repositories import ContractorRepository

from .base_entity_service import BaseEntityService


class ContractorService(BaseEntityService):
    def __init__(self) -> None:
        self._repository = ContractorRepository()
