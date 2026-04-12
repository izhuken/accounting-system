from core.service.app import WarehouseService

from .base_commands import BaseRemoveCommand


class WarehouseRemoveCommand(BaseRemoveCommand):
    service = WarehouseService
