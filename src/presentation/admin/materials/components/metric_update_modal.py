from core.domain.entities import Metric
from core.domain.repositories.exc import SaveException
from core.domain.value_objects.metric import MetricCode
from core.service.app import MetricService
from shared.components.common_input import CommonInput
from shared.components.form import CommonUpdateModal
from shared.lib import SnackBarType, snack


class MetricUpdateModal(CommonUpdateModal):
    modal_title: str = "Редактирование метрики"
    topic_name: str = "metric_list_page__refetch"
    entity = Metric
    entity_service = MetricService

    def __init__(self, payload: dict):
        super().__init__(
            payload,
            {
                "name": CommonInput(label="Наименование"),
            },
        )

    def update_entity(self, payload: dict, entity: Metric) -> Metric:
        entity.update_name(payload.get("name"))
        return entity

    async def submit(self, *args, **kwargs):
        payload = self._complect_fields()
        service = self.entity_service()

        entity = await service.one(MetricCode(self.payload.get("code")))

        try:
            updated_entity = self.update_entity(payload, entity)
            await service.save(updated_entity)
        except (SaveException, ValueError) as e:
            return snack(self.page, str(e), SnackBarType.ERROR)

        self.close()
        self.page.pubsub.send_all_on_topic(self.topic_name, "refresh")
        snack(self.page, "Успешно!", SnackBarType.SUCCESS)
