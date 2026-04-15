from core.service.app import ProductService
from core.service.command import ProductRemoveCommand
from shared.components.common_actions_view import CommonActionsColumn

from .product_update_modal import ProductUpdateModal


class ProductActionsView(CommonActionsColumn):
    service = ProductService
    modal = ProductUpdateModal
    topic_name = "product_list_page__refetch"
    remove_command = ProductRemoveCommand
