from core.domain.entities import Material
from core.service.app import MaterialService
from core.service.app.metric_service import MetricService
from shared.components.common_input import CommonInput
from shared.components.custom_dropdown import CustomDropdown
from shared.components.form import CommonCreateModal


class MaterialCreateModal(CommonCreateModal):
    modal_title = "Новый материал"
    topic_name = "material_list_page__refetch"
    entity = Material
    entity_service = MaterialService

    def __init__(self):
        super().__init__(
            {
                "name": CommonInput(label="Наименование"),
                "metric": CustomDropdown(
                    label="Метрика",
                    service=MetricService(),
                    option_selector="name",
                    option_key_selector="code",
                    expand=True,
                ),
            }
        )

    def create_entity(self, payload: dict) -> Material:
        return Material.create(name=payload.get("name"), metric=payload.get("metric"))
