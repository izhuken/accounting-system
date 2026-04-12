from core.infrastructure.sqlite.repositories import ClientRepository

from .base_entity_service import BaseEntityService


class ClientService(BaseEntityService):
    def __init__(self) -> None:
        self._repository = ClientRepository()
