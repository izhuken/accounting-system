from core.service.app import ClientService
from core.service.command import ClientRemoveCommand
from shared.components.common_actions_view import CommonActionsColumn

from .update_modal import ClientUpdateModal


class ActionsView(CommonActionsColumn):
    service = ClientService
    modal = ClientUpdateModal
    topic_name = "client_list_page__refetch"
    remove_command = ClientRemoveCommand
