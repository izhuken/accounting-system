from asyncio import create_task

from flet import ButtonStyle, ControlState, FilledButton, MouseCursor, Ref, Text

from shared.colors import Colors
from shared.lib.router import Router


class TabButton(FilledButton):
    def __init__(self, title: str, route: str, router: Router):
        self._route = route
        self.router = router
        self._is_disabled = False
        self._text_ref = Ref[Text]()

        super().__init__(
            content=Text(
                title,
                color=Colors.TEXT_DARK,
                ref=self._text_ref,
            ),
            on_click=lambda _: router.page.go(route),
            disabled=self._is_disabled,
            bgcolor={
                ControlState.DEFAULT: Colors.BACKGROUND,
                ControlState.DISABLED: Colors.BLUE_DARK,
            },
            style=ButtonStyle(
                shadow_color=Colors.TRANSPARENT,
                overlay_color=Colors.TRANSPARENT,
                mouse_cursor=MouseCursor.CLICK,
            ),
        )

        create_task(self.update_state())

    async def update_state(self):
        self._is_disabled = self.router.is_current_page(self._route, True)
        self.disabled = self._is_disabled
        self._text_ref.current.color = (
            Colors.BACKGROUND if self._is_disabled else Colors.TEXT_DARK
        )
        self._text_ref.current.update()
        self.update()
