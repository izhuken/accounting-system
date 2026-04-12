from typing import Any
from uuid import UUID

from flet import (
    AlertDialog,
    Alignment,
    ButtonStyle,
    Column,
    FontWeight,
    MouseCursor,
    Text,
    TextButton,
)

from core.domain.entities.entity import Entity
from core.domain.repositories.exc import SaveException
from core.service.app.ientity_service import IEntityService
from shared.colors import Colors
from shared.components.common_button import CommonButton
from shared.components.common_input import CommonInput
from shared.lib import SnackBarType, is_uuid, snack


class CommonCreateModal(AlertDialog):
    modal_title: str
    topic_name: str
    entity: Entity
    entity_service: IEntityService
    height: int | float | None = None

    def __init__(self, fields: dict[str, CommonInput]) -> None:
        self.fields = fields

        super().__init__(
            title=Text(
                self.modal_title,
                weight=FontWeight.W_600,
                size=32,
                color=Colors.TEXT_DARK,
            ),
            content=Column(
                [field for field in self.fields.values()]
                + [CommonButton("Создать", self.submit)],
                height=self.height if self.height else len(self.fields) * 60 + 60,
                alignment=Alignment.CENTER,
            ),
            actions=[
                TextButton(
                    "Закрыть",
                    on_click=self.close,
                    style=ButtonStyle(mouse_cursor=MouseCursor.CLICK),
                ),
            ],
            bgcolor=Colors.BACKGROUND,
            actions_alignment=Alignment.CENTER,
        )

    async def submit(self, *args, **kwargs):
        payload = self._complect_fields()

        try:
            new_entity = self.create_entity(payload)
        except ValueError as e:
            return snack(self.page, str(e), SnackBarType.ERROR)

        try:
            service = self.entity_service()
            await service.save(new_entity)
        except SaveException as e:
            return snack(self.page, str(e), SnackBarType.ERROR)

        self.close()
        self.page.pubsub.send_all_on_topic(self.topic_name, "refresh")
        snack(self.page, "Успешно!", SnackBarType.SUCCESS)

    def create_entity(self, payload: dict) -> Entity:
        raise NotImplementedError

    def close(self, *args, **kwargs):
        for field in self.fields.values():
            field.clean_field()

        self.page.pop_dialog()

    def _complect_fields(self) -> dict[str, Any]:
        payload = {}

        for field_name, field_value in self.fields.items():
            if is_uuid(str(field_value.value)):
                payload[field_name] = UUID(field_value.value)
                continue

            payload[field_name] = field_value.value

        return payload
