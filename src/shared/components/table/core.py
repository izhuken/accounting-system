from typing import Callable

from flet import (
    Column,
    Container,
    Ref,
    Row,
    ScrollbarTheme,
    Theme,
)

from ._connector import AddConnector
from ._footer import TableFooter
from ._header import TableHeader, TableHeaderPosition
from ._row import TableRow
from .dto import TableAccessor, TableData


class Table(Container):
    def __init__(
        self,
        accessors: list[TableAccessor] = [],
        payload: TableData = TableData(),
        topic_name: str | None = None,
        on_add: Callable | None = None,
        on_row_click: Callable | None = None,
        ref: Ref[Container] = None,
    ):
        self.data = []
        self.editable = False

        self.topic_name = topic_name
        self.accessors = accessors
        self.payload = payload
        self.on_row_click = on_row_click

        self.header_content = Row([], spacing=0)
        self.table_content = Column(
            controls=[], spacing=0, expand=True, expand_loose=True, scroll="always"
        )
        self.table_connector = AddConnector(on_add) if on_add else Container()
        self.table_footer = TableFooter(self.payload, self.topic_name)

        super().__init__(
            content=Column(
                [
                    self.header_content,
                    self.table_content,
                    self.table_connector,
                    self.table_footer,
                ],
                spacing=0,
            ),
            ref=ref,
            theme=Theme(scrollbar_theme=ScrollbarTheme(thickness=0)),
            expand=True,
        )

    def did_mount(self):
        self._render_header()
        if len(self.payload.data) != 0:
            self._refresh_table()

    def refresh(self, payload: TableData):
        self.payload = payload
        self._refresh_table()

    def disable(self):
        if not self.table_connector:
            return

        self.table_connector.disable()

    def _refresh_table(self):
        if not self.accessors:
            return

        self.table_content.controls.clear()

        for entity in self.payload.data:
            self.table_content.controls.append(
                TableRow(self.accessors, entity, self.on_row_click)
            )

        self.table_content.update()
        self.table_footer.refresh(self.payload)

    def _render_header(self):
        self.header_content.controls.clear()

        for index, column in enumerate(self.accessors):
            position = TableHeaderPosition.COMMON

            if index == 0:
                position = TableHeaderPosition.FIRST

            if index == len(self.accessors) - 1:
                position = TableHeaderPosition.LAST

            if len(self.accessors) == 1:
                position = TableHeaderPosition.ONCE

            header_cell = TableHeader(
                label=column.header,
                width=column.width,
                expand=column.expand,
                position=position,
            )

            self.header_content.controls.append(header_cell)

        self.header_content.update()
