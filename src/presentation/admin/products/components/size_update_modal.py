from core.domain.entities import Size
from core.domain.repositories.exc import SaveException
from core.domain.value_objects.size import SizeCode
from core.service.app import SizeService
from shared.components.common_input import CommonInput
from shared.components.form import CommonUpdateModal
from shared.lib import SnackBarType, snack


class SizeUpdateModal(CommonUpdateModal):
    modal_title: str = "Редактирование размера"
    topic_name: str = "size_list_page__refetch"
    entity = Size
    entity_service = SizeService

    def __init__(self, payload: dict):
        super().__init__(
            payload,
            {
                "height": CommonInput(label="Рост"),
            },
        )

    def update_entity(self, payload: dict, entity: Size) -> Size:
        entity.update_height(payload.get("height"))
        return entity

    async def submit(self, *args, **kwargs):
        payload = self._complect_fields()
        service = self.entity_service()

        entity = await service.one(SizeCode(self.payload.get("code")))

        try:
            updated_entity = self.update_entity(payload, entity)
            await service.save(updated_entity)
        except (SaveException, ValueError) as e:
            return snack(self.page, str(e), SnackBarType.ERROR)

        self.close()
        self.page.pubsub.send_all_on_topic(self.topic_name, "refresh")
        snack(self.page, "Успешно!", SnackBarType.SUCCESS)
