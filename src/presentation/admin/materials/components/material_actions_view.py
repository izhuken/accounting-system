from core.service.app import MaterialService
from core.service.command import MaterialRemoveCommand
from shared.components.common_actions_view import CommonActionsColumn

from .material_update_modal import MaterialUpdateModal


class MaterialActionsView(CommonActionsColumn):
    service = MaterialService
    modal = MaterialUpdateModal
    topic_name = "material_list_page__refetch"
    remove_command = MaterialRemoveCommand
