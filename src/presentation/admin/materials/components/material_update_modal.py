from core.domain.entities import Material
from core.service.app import MaterialService, MetricService
from shared.components.common_input import CommonInput
from shared.components.custom_dropdown import CustomDropdown
from shared.components.form import CommonUpdateModal


class MaterialUpdateModal(CommonUpdateModal):
    modal_title: str = "Редактирование материала"
    topic_name: str = "material_list_page__refetch"
    entity = Material
    entity_service = MaterialService

    def __init__(self, payload: dict):
        super().__init__(
            payload,
            {
                "name": CommonInput(label="Наименование"),
                "metric": CustomDropdown(
                    label="Метрика",
                    service=MetricService(),
                    option_selector="name",
                    option_key_selector="code",
                    expand=True,
                ),
            },
        )

    def update_entity(self, payload: dict, entity: Material) -> Material:
        entity.update_name(payload.get("name"))
        entity.update_metric(payload.get("metric"))
        return entity
