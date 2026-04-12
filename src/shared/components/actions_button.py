from typing import Callable

from flet import (
    Container,
    CupertinoButton,
    Image,
    Ref,
    Row,
    alignment,
    border,
    padding,
)

from shared.colors import Colors
from shared.lib.asset import assets


class ActionsButton(Container):
    def __init__(
        self,
        image: str,
        color: str,
        action: Callable = lambda x: None,
        disabled: bool = False,
        visible: bool = True,
        ref: Ref = None,
    ):
        self._image_ref = Ref[Image]()
        self._button_ref = Ref[CupertinoButton]()

        super().__init__(
            CupertinoButton(
                content=Row(
                    [
                        Image(
                            assets(image),
                            height=16,
                            width=16,
                            ref=self._image_ref,
                            color=color,
                        )
                    ],
                    alignment=alignment.Alignment.CENTER,
                ),
                bgcolor=Colors.WHITE,
                height=32,
                width=32,
                padding=padding.only(left=6),
                alignment=alignment.Alignment.CENTER,
                border_radius=5,
                on_click=action,
                ref=self._button_ref,
                disabled=disabled,
            ),
            border=border.all(1.2, color),
            border_radius=5,
            height=32,
            width=32,
            ref=ref,
            disabled=disabled,
            visible=visible,
        )

        if disabled:
            self.disable()
