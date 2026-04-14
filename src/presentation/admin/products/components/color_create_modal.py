from core.domain.entities import Color
from core.service.app import ColorService
from shared.components.form import CommonCreateModal
from shared.components.numeric_input import NumericInput


class ColorCreateModal(CommonCreateModal):
    modal_title = "Новый цвет"
    topic_name = "color_list_page__refetch"
    entity = Color
    entity_service = ColorService

    def __init__(self):
        super().__init__(
            {
                "name": NumericInput(label="Наименование"),
            }
        )

    def create_entity(self, payload: dict) -> Color:
        return Color.create(
            name=payload.get("name"),
        )
