from core.domain.entities import Product
from core.service.app import ColorService, ProductService, SizeService
from shared.components.common_input import CommonInput
from shared.components.custom_dropdown import CustomDropdown
from shared.components.form import CommonUpdateModal


class ProductUpdateModal(CommonUpdateModal):
    modal_title: str = "Редактирование продукта"
    topic_name: str = "product_list_page__refetch"
    entity = Product
    entity_service = ProductService

    def __init__(self, payload: dict):
        super().__init__(
            payload,
            {
                "name": CommonInput(label="Наименование"),
                "size": CustomDropdown(
                    label="Размер",
                    service=SizeService(),
                    option_selector="code",
                    option_key_selector="code",
                    expand=True,
                ),
                "color": CustomDropdown(
                    label="Цвет",
                    service=ColorService(),
                    option_selector="name",
                    expand=True,
                ),
            },
        )

    def update_entity(self, payload: dict, entity: Product) -> Product:
        entity.update_name(payload.get("name"))
        entity.update_size(payload.get("size"))
        entity.update_color(payload.get("color"))
        return entity
