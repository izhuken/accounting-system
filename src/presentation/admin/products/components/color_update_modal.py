from core.domain.entities import Color
from core.service.app import ColorService
from shared.components.common_input import CommonInput
from shared.components.form import CommonUpdateModal


class ColorUpdateModal(CommonUpdateModal):
    modal_title: str = "Редактирование размера"
    topic_name: str = "Color_list_page__refetch"
    entity = Color
    entity_service = ColorService

    def __init__(self, payload: dict):
        super().__init__(
            payload,
            {
                "name": CommonInput(label="Наименование"),
            },
        )

    def update_entity(self, payload: dict, entity: Color) -> Color:
        entity.update_name(payload.get("name"))
        return entity
