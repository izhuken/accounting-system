from core.service.app import ContractorService
from core.service.command import ContractorRemoveCommand
from shared.components.common_actions_view import CommonActionsColumn

from .update_modal import ContractorUpdateModal


class ActionsView(CommonActionsColumn):
    service = ContractorService
    modal = ContractorUpdateModal
    topic_name = "contractor_list_page__refetch"
    remove_command = ContractorRemoveCommand
