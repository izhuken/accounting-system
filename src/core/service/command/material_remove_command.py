from core.service.app import MaterialService

from .base_commands import BaseRemoveCommand


class MaterialRemoveCommand(BaseRemoveCommand):
    service = MaterialService
