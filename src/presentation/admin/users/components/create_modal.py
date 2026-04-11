from flet import TextField

from app.components.common import toast
from app.components.form import CommonCreateModal
from app.components.styles import COLORS
from dto.app import DBusUpdateCommand
from dto.exc import CreateError
from services.db import UserService
from services.dbus import DBUS


class CreateModal(CommonCreateModal):
    alert_title: str = "Добавление пользователя"
    topic_name: str = "users"
    service: UserService = UserService()
    fields = {
        "username": TextField(
            label="Имя пользователя",
            color=COLORS["brown_main"],
            expand=True,
            expand_loose=True,
        ),
        "password": TextField(
            label="Пароль", color=COLORS["brown_main"], expand=True, expand_loose=True
        ),
    }

    async def submit(self, *args, **kwargs):
        payload = self._complect_fields()

        try:
            result = await self.service.add_user(**payload)
        except CreateError as e:
            return toast(self.page, e.message, "error")

        self.close()
        toast(self.page, "Успешно! Пользователь успешно создан!", "success")
        DBUS.send(self.topic_name, DBusUpdateCommand(self.topic_name, True))
