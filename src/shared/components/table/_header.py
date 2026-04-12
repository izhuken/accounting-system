from enum import Enum

from flet import Container, FontWeight, Text, border, border_radius

from shared.colors import Colors


class TableHeaderPosition(Enum):
    FIRST = "first"
    LAST = "last"
    COMMON = "common"
    ONCE = "once"


class TableHeader(Container):
    def __init__(
        self,
        label: str,
        width: int | float = None,
        expand: bool = False,
        position: TableHeaderPosition = TableHeaderPosition.COMMON,
    ):
        __radiuses = {
            TableHeaderPosition.FIRST: border_radius.only(top_left=5),
            TableHeaderPosition.LAST: border_radius.only(top_right=5),
            TableHeaderPosition.ONCE: border_radius.only(top_left=5, top_right=5),
            TableHeaderPosition.COMMON: border_radius.only(top_left=0, top_right=0),
        }

        super().__init__(
            content=Text(label, weight=FontWeight.W_600, size=14, color=Colors.WHITE),
            width=width,
            expand=expand,
            padding=10,
            border=border.all(1, Colors.TEXT_DARK),
            bgcolor=Colors.BLUE_OCEAN,
            border_radius=__radiuses[position],
        )
