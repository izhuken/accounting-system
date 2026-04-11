from flet import AlertDialog, Column, FontWeight, Text, TextButton, TextField, alignment

from app.components.common import BrownButton, toast
from app.components.styles import COLORS
from dto.app import DBusUpdateCommand
from dto.exc import ProcessingError
from services.db import DBConverterService, UserService
from services.dbus import DBUS


class ChangePasswordModal(AlertDialog):
    alert_title: str = "Обновление пароля"
    topic_name: str = "users"
    service: UserService = UserService()
    fields = {
        "password": TextField(
            label="Пароль",
            color=COLORS["brown_main"],
        ),
    }

    def __init__(self, payload: dict):
        self.payload = payload

        super().__init__(
            modal=True,
            adaptive=True,
            title=Text(
                self.alert_title,
                weight=FontWeight.W_600,
                size=32,
                color=COLORS["brown_main"],
                expand=True,
                expand_loose=True,
            ),
            content=Column(
                [field for field in self.fields.values()]
                + [
                    BrownButton("Обновить", self.submit),
                ],
                alignment=alignment.Alignment.CENTER,
                height=len(self.fields) * 60 + 60,
            ),
            actions=[
                TextButton(
                    "Закрыть",
                    on_click=self.close,
                ),
            ],
            bgcolor=COLORS["gray_bg"],
            actions_alignment=alignment.Alignment.CENTER,
        )

    async def submit(self, *args, **kwargs):
        try:
            result = await self.service.change_password(
                DBConverterService.to_uuid(self.payload.get("id")),
                self.fields.get("password").value,
            )
        except ProcessingError as e:
            return toast(self.page, e.message, "error")

        self.close()
        toast(self.page, "Успешно! Пользователь успешно обновлен!", "success")
        DBUS.send(self.topic_name, DBusUpdateCommand(self.topic_name, True))

    def close(self, *args, **kwargs):
        for field in self.fields.values():
            field.value = None

        self.page.pop_dialog()
