from typing import Callable

from flet import (
    CupertinoButton,
    MouseCursor,
    Row,
    Text,
    TextAlign,
    border_radius,
    padding,
)

from shared.colors import Colors


class CommonButton(CupertinoButton):
    def __init__(
        self,
        text: str,
        on_click: Callable = lambda x: None,
        disabled: bool = False,
        expand: bool | int | None = None,
    ):
        super().__init__(
            content=Row(
                [
                    Text(
                        text,
                        text_align=TextAlign.CENTER,
                        expand=1,
                        color=Colors.WHITE,
                    )
                ]
            ),
            on_click=on_click,
            padding=padding.all(16.0),
            border_radius=border_radius.all(5),
            mouse_cursor=MouseCursor.CLICK,
            bgcolor=Colors.BLUE_DARK,
            disabled=disabled,
            expand=expand,
        )
