from core.service.app import ProductService

from .base_commands import BaseRemoveCommand


class ProductRemoveCommand(BaseRemoveCommand):
    service = ProductService
