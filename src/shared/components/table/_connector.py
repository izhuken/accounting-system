from typing import Callable

from flet import (
    Container,
    CupertinoButton,
    Image,
    MainAxisAlignment,
    MouseCursor,
    Ref,
    Row,
    border,
)

from shared.colors import Colors
from shared.lib.asset import assets


class AddConnector(Container):
    def __init__(self, cb: Callable | None, disabled: bool = False, ref=None):
        self._button_ref = Ref[CupertinoButton]()
        self._image_ref = Ref[Image]()

        self._image_color_config = {
            "active": Colors.WHITE,
            "disabled": Colors.GRAY_DISABLED,
        }

        super().__init__(
            Row(
                [
                    CupertinoButton(
                        content=Row(
                            [
                                Image(
                                    assets("icons/plus.svg"),
                                    height=10,
                                    width=10,
                                    color=self._image_color_config["active"],
                                    ref=self._image_ref,
                                )
                            ],
                        ),
                        bgcolor=Colors.BLUE_DARK,
                        disabled_bgcolor=Colors.GRAY_DISABLED,
                        mouse_cursor=MouseCursor.CLICK,
                        height=32,
                        width=32,
                        padding=10,
                        on_click=cb,
                        disabled=disabled,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
                height=42,
            ),
            height=50,
            border=border.all(1, Colors.BLACK),
            ref=ref,
            bgcolor=Colors.BACKGROUND,
        )
