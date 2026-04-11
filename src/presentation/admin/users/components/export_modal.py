from typing import Any
from uuid import UUID

from flet import (
    AlertDialog,
    Column,
    FilePicker,
    FontWeight,
    Text,
    TextButton,
    alignment,
)

from app.components.common import BrownButton, CustomDropdown, toast
from app.components.styles import COLORS
from dto.app import DBusUpdateCommand
from services.db import (
    ContractorService,
    DBConverterService,
    OrderService,
    StockService,
    UserService,
)
from services.dbus import DBUS
from services.dumper import SQLiteDumper


class ExportModal(AlertDialog):
    alert_title: str = "Экспорт данных"
    topic_name: str = "users"
    service: UserService = UserService()
    fields = {
        "order_id": CustomDropdown(
            label="Заказ",
            service=OrderService(),
            option_selector=lambda x: f"Заказ №{x.id}",
            topic="orders",
            width=400,
        ),
        "contractor_id": CustomDropdown(
            label="Исполнитель",
            service=ContractorService(),
            option_selector=lambda x: x.name,
            topic="contractors",
            width=400,
        ),
        "stock_id": CustomDropdown(
            label="Склад исполнителя",
            service=StockService(),
            option_selector=lambda x: x.name,
            topic="stocks",
            width=400,
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
        file_picker = FilePicker()
        directory = await file_picker.get_directory_path("Выберите папку для экспорта")

        if not directory:
            return toast(self.page, "Папка не выбрана!", "error")

        form_values = self._complect_fields()

        if not form_values.get("order_id"):
            return toast(self.page, "Заказ не выбран!", "error")

        if not form_values.get("contractor_id"):
            return toast(self.page, "Исполнитель не выбран!", "error")

        if not form_values.get("stock_id"):
            return toast(self.page, "Склад исполнителя не выбран!", "error")

        form_values = form_values | {
            "export_folder": directory,
            "user_id": self.payload.get("id"),
            "order_id": int(form_values.get("order_id")),
        }

        dumper = SQLiteDumper()

        self.close()

        try:
            dumper.export_for_contractor(**form_values)
        except Exception:
            return toast(self.page, "Ошибка! Не удалось выгрузить данные!", "error")

        toast(self.page, "Успешно! Данные успешно выгружены!", "success")
        DBUS.send(self.topic_name, DBusUpdateCommand(self.topic_name, True))

    def close(self, *args, **kwargs):
        for field in self.fields.values():
            field.value = None

        self.page.pop_dialog()

    def _complect_fields(self) -> dict[str, Any]:
        payload = {}

        for field_name, field_value in self.fields.items():
            if DBConverterService.is_uuid(str(field_value.value)):
                payload[field_name] = UUID(field_value.value)
                continue

            payload[field_name] = field_value.value

        return payload
