from core.domain.entities import Size
from core.service.app import SizeService
from shared.components.common_input import CommonInput
from shared.components.form import CommonCreateModal
from shared.components.numeric_input import NumericInput


class SizeCreateModal(CommonCreateModal):
    modal_title = "Новый размер"
    topic_name = "size_list_page__refetch"
    entity = Size
    entity_service = SizeService

    def __init__(self):
        super().__init__(
            {
                "code": NumericInput(label="Размер"),
                "height": CommonInput(label="Рост"),
            }
        )

    def create_entity(self, payload: dict) -> Size:
        return Size.create(
            code=payload.get("code"),
            height=payload.get("height"),
        )
