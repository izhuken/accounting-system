from inspect import iscoroutinefunction
from typing import Callable

from flet import Container, FontWeight, Row, Text, alignment

from shared.colors import Colors

from ._cell import TableCell
from .dto import TableAccessor


class TableRow(Container):
    def __init__(
        self,
        accessors: list[TableAccessor],
        payload: dict,
        on_row_click: Callable | None = None,
    ):
        self.__payload = payload
        self.__on_row_click = on_row_click
        super().__init__(
            Row(
                [
                    TableCell(
                        Container(
                            Text(
                                self._get_value(accessor),
                                weight=FontWeight.W_500,
                                color=Colors.TEXT_DARK,
                            ),
                            padding=10,
                            alignment=alignment.Alignment.CENTER_LEFT,
                        )
                        if not accessor.view
                        else accessor.view(payload),
                        width=accessor.width,
                        expand=accessor.expand,
                    )
                    for accessor in accessors
                ],
                spacing=0,
                expand=True,
            ),
            on_click=self._call_on_click,
        )

    def _get_value(self, accessor: TableAccessor):
        if accessor.value is not None:
            return accessor.value(self.__payload)

        field_chain = [accessor.accessor]
        value = self.__payload

        if "__" in accessor.accessor:
            field_chain = accessor.accessor.split("__")

        for sub_field in field_chain:
            if not value:
                return ""

            value = value.get(sub_field)

        return value

    async def _call_on_click(self, *args, **kwargs):
        if not self.__on_row_click:
            return

        if iscoroutinefunction(self.__on_row_click):
            return await self.__on_row_click(self.__payload)

        return self.__on_row_click(self.__payload)
