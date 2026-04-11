from flet import TextField

from app.components.common import toast
from app.components.form import CommonUpdateModal
from app.components.styles import COLORS
from dto.app import DBusUpdateCommand
from dto.exc import ProcessingError
from services.db import DBConverterService, UserService
from services.dbus import DBUS


class UpdateUsernameModal(CommonUpdateModal):
    alert_title: str = "Обновление пользователя"
    topic_name: str = "users"
    service: UserService = UserService()
    fields = {
        "username": TextField(
            label="Имя пользователя",
            color=COLORS["brown_main"],
            expand=True,
            expand_loose=True,
        ),
    }

    async def submit(self, *args, **kwargs):
        try:
            result = await self.service.update_username(
                DBConverterService.to_uuid(self.payload.get("id")),
                self.fields.get("username").value,
            )
        except ProcessingError as e:
            return toast(self.page, e.message, "error")

        self.close()
        toast(self.page, "Успешно! Пользователь успешно обновлен!", "success")
        DBUS.send(self.topic_name, DBusUpdateCommand(self.topic_name, True))
