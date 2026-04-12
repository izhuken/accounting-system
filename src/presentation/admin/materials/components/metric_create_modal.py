from core.domain.entities import Metric
from core.service.app import MetricService
from shared.components.common_input import CommonInput
from shared.components.form import CommonCreateModal
from shared.components.numeric_input import NumericInput


class MetricCreateModal(CommonCreateModal):
    modal_title = "Новая метрика"
    topic_name = "metric_list_page__refetch"
    entity = Metric
    entity_service = MetricService

    def __init__(self):
        super().__init__(
            {
                "code": NumericInput(label="Код"),
                "name": CommonInput(label="Наименование"),
            }
        )

    def create_entity(self, payload: dict) -> Metric:
        return Metric.create(
            code=payload.get("code"),
            name=payload.get("name"),
        )
