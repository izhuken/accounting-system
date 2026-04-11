from flet import CrossAxisAlignment, MainAxisAlignment, Row

from shared.colors import Colors
from shared.components.actions_button import ActionsButton


class ActionsView(Row):
    def __init__(self, payload: dict):
        self.payload = payload

        super().__init__(
            [
                ActionsButton(
                    "icons/edit.svg",
                    Colors.TEXT_DARK,
                    # self.open_change_username_modal,
                ),
                ActionsButton(
                    "icons/pin.svg",
                    Colors.TEXT_DARK,
                    # self.open_change_password_modal,
                ),
                ActionsButton(
                    "icons/export.svg",
                    Colors.TEXT_DARK,
                    # self.open_export_modal,
                ),
                ActionsButton(
                    "icons/delete.svg",
                    Colors.RED_ACCENT,
                    # self.delete_item,
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
        )

    # async def open_change_username_modal(self, *args, **kwargs):
    #     self.page.show_dialog(UpdateUsernameModal(self.payload))

    # async def open_change_password_modal(self, *args, **kwargs):
    #     self.page.show_dialog(ChangePasswordModal(self.payload))

    # async def open_export_modal(self):
    #     self.page.show_dialog(ExportModal(self.payload))

    # async def delete_item(self, *args, **kwargs):
    #     result = await self.service.delete(self.payload.get("id"))

    #     if isinstance(result, ErrorResponse):
    #         return toast(self.page, "Ошибка! Не удалось удалить запись!", "error")

    #     toast(self.page, "Успешно!", "success")
    #     DBUS.send("users", DBusUpdateCommand("users", "update"))
