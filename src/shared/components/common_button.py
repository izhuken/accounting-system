from typing import Callable

from flet import (
    ControlState,
    CupertinoButton,
    Ref,
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
        ref: Ref[CupertinoButton] | None = None,
    ):
        self._text_ref = Ref[Text]()

        self._text_color_config = {
            "active": Colors.WHITE,
            "disabled": Colors.TEXT_DISABLED,
        }

        super().__init__(
            content=Row(
                [
                    Text(
                        text,
                        text_align=TextAlign.CENTER,
                        expand=1,
                        color=self._text_color_config["active"],
                        ref=self._text_ref,
                    )
                ]
            ),
            on_click=on_click,
            padding=padding.all(16.0),
            border_radius=border_radius.all(5),
            bgcolor=Colors.BLUE_DARK,
            disabled_bgcolor=Colors.GRAY_DISABLED,
            color={
                ControlState.DEFAULT: Colors.WHITE,
                ControlState.DISABLED: Colors.GRAY_DISABLED,
            },
            disabled=disabled,
            expand=expand,
            ref=ref,
        )

    def enable(self):
        if not self.disabled:
            return

        self.disabled = False
        self._text_ref.current.color = self._text_color_config["active"]
        self.update()
        self._text_ref.current.update()

    def disable(self):
        if self.disabled:
            return

        self.disabled = True
        self._text_ref.current.color = self._text_color_config["disabled"]
        self.update()
        self._text_ref.current.update()
