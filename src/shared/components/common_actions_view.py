from flet import AlertDialog, CrossAxisAlignment, MainAxisAlignment, Row

from core.domain.repositories.exc.remove import RemoveException
from core.service.app.ientity_service import IEntityService
from core.service.command.base_commands import BaseRemoveCommand
from shared.colors import Colors
from shared.components.actions_button import ActionsButton
from shared.lib import SnackBarType, snack


class CommonActionsColumn(Row):
    service: IEntityService
    modal: AlertDialog | None = None
    topic_name: str
    remove_command: BaseRemoveCommand
    components: list[str] = ["update", "delete"]

    def __init__(self, payload: dict):
        self.payload = payload

        super().__init__(
            [
                ActionsButton(
                    "icons/edit.svg",
                    Colors.TEXT_DARK,
                    self.update_item,
                    visible="update" in self.components,
                ),
                ActionsButton(
                    "icons/delete.svg",
                    Colors.RED_ACCENT,
                    self.delete_item,
                    visible="delete" in self.components,
                ),
            ],
            spacing=5,
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
        )

    async def update_item(self, *args, **kwargs):
        if not self.modal:
            return

        self.page.show_dialog(self.modal(self.payload))

    async def delete_item(self, *args, **kwargs):
        command = self.remove_command()
        try:
            await command.execute(self.payload.get("id"))
        except RemoveException as e:
            return snack(self.page, e.message, SnackBarType.ERROR)

        snack(self.page, "Запись успешно удалена!")
        self.page.pubsub.send_all_on_topic(self.topic_name, "refresh")
