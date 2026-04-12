from core.service.app import WarehouseService
from core.service.command import WarehouseRemoveCommand
from shared.components.common_actions_view import CommonActionsColumn

from .update_modal import WarehouseUpdateModal


class ActionsView(CommonActionsColumn):
    service = WarehouseService
    modal = WarehouseUpdateModal
    topic_name = "warehouse_list_page__refetch"
    remove_command = WarehouseRemoveCommand
