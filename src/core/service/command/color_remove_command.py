from core.service.app import ColorService

from .base_commands import BaseRemoveCommand


class ColorRemoveCommand(BaseRemoveCommand):
    service = ColorService
