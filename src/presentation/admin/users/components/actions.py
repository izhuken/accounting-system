from flet import CrossAxisAlignment, MainAxisAlignment, Row

from core.service.command import UserRemoveCommand
from presentation.admin.users.components.change_password import PasswordUpdateModal
from shared.colors import Colors
from shared.components.actions_button import ActionsButton
from shared.lib import snack

from .change_username import UsernameUpdateModal


class ActionsView(Row):
    topic_name: str = "user_list_page__refetch"

    def __init__(self, payload: dict):
        self.payload = payload

        super().__init__(
            [
                ActionsButton(
                    "icons/edit.svg",
                    Colors.TEXT_DARK,
                    self.open_change_username_modal,
                ),
                ActionsButton(
                    "icons/pin.svg",
                    Colors.TEXT_DARK,
                    self.open_change_password_modal,
                ),
                ActionsButton(
                    "icons/export.svg",
                    Colors.TEXT_DARK,
                    # self.open_export_modal,
                ),
                ActionsButton(
                    "icons/delete.svg",
                    Colors.RED_ACCENT,
                    self.delete_user,
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
        )

    async def open_change_username_modal(self, *args, **kwargs):
        self.page.show_dialog(UsernameUpdateModal(self.payload))

    async def open_change_password_modal(self, *args, **kwargs):
        self.page.show_dialog(PasswordUpdateModal(self.payload))

    # async def open_export_modal(self):
    #     self.page.show_dialog(ExportModal(self.payload))

    async def delete_user(self):
        command = UserRemoveCommand()
        await command.execute(self.payload.get("id"))
        snack(self.page, "Запись успешно удалена!")
        self.page.pubsub.send_all_on_topic(self.topic_name, "refresh")
