from typing import Any

from flet import Container, border

from shared.colors import Colors


class TableCell(Container):
    def __init__(self, content: Any, width: int | float = None, expand: bool = False):
        super().__init__(
            content=content,
            width=width,
            padding=0,
            border=border.all(1, Colors.TEXT_DARK),
            bgcolor=Colors.WHITE,
            expand=expand,
            height=50,
        )
