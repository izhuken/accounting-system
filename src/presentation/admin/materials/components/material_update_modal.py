from core.domain.entities import Material
from core.service.app import MaterialService
from shared.components.common_input import CommonInput
from shared.components.form import CommonUpdateModal


class MaterialUpdateModal(CommonUpdateModal):
    modal_title: str = "Редактирование материала"
    topic_name: str = "material_list_page__refetch"
    entity = Material
    entity_service = MaterialService

    def __init__(self, payload: dict):
        super().__init__(
            payload,
            {"name": CommonInput(label="Наименование")},
        )

    def update_entity(self, payload: dict, entity: Material) -> Material:
        entity.update_name(payload.get("name"))
        return entity
