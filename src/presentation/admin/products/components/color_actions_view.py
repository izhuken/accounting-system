from core.service.app import ColorService
from core.service.command import ColorRemoveCommand
from shared.components.common_actions_view import CommonActionsColumn

from .color_update_modal import ColorUpdateModal


class ColorActionsView(CommonActionsColumn):
    service = ColorService
    modal = ColorUpdateModal
    topic_name = "color_list_page__refetch"
    remove_command = ColorRemoveCommand
