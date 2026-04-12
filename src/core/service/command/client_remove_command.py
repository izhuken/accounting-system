from core.service.app import ClientService

from .base_commands import BaseRemoveCommand


class ClientRemoveCommand(BaseRemoveCommand):
    service = ClientService
