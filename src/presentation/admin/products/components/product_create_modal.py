from core.domain.entities import Product
from core.service.app import ColorService, ProductService, SizeService
from shared.components.common_input import CommonInput
from shared.components.custom_dropdown import CustomDropdown
from shared.components.form import CommonCreateModal


class ProductCreateModal(CommonCreateModal):
    modal_title = "Новый товар"
    topic_name = "product_list_page__refetch"
    entity = Product
    entity_service = ProductService

    def __init__(self):
        super().__init__(
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
            }
        )

    def create_entity(self, payload: dict) -> Product:
        return Product.create(
            name=payload.get("name"),
            size=payload.get("size"),
            color=payload.get("color"),
        )
