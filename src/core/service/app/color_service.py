from core.infrastructure.sqlite.repositories import ColorRepository

from .base_entity_service import BaseEntityService


class ColorService(BaseEntityService):
    def __init__(self) -> None:
        self._repository = ColorRepository()
