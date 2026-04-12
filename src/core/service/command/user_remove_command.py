from core.service.app import UserService

from .base_commands import BaseRemoveCommand


class UserRemoveCommand(BaseRemoveCommand):
    service = UserService
