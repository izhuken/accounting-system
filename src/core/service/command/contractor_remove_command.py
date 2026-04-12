from core.service.app import ContractorService

from .base_commands import BaseRemoveCommand


class ContractorRemoveCommand(BaseRemoveCommand):
    service = ContractorService
