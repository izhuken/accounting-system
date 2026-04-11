from flet import (
    ButtonStyle,
    CircleAvatar,
    Column,
    Container,
    Divider,
    Image,
    MouseCursor,
    PopupMenuButton,
    PopupMenuItem,
    Ref,
    Row,
    Text,
    padding,
)

from core.service.app import UserService
from shared.colors import Colors
from shared.components.spacer import Spacer
from shared.lib.asset import assets
from shared.lib.cache import CacheService

FOOTER_CACHE = CacheService()


class NavFooter(Column):
    def __init__(self):
        self.__username_ref = Ref[Text]()
        self.__avatar_ref = Ref[Text]()

        try:
            self._username = FOOTER_CACHE.get("username")
        except Exception:
            self._username = ""

        super().__init__(
            controls=[
                Divider(color=Colors.WHITE, thickness=1, height=1),
                Container(
                    Row(
                        [
                            CircleAvatar(
                                content=Text(
                                    "?",
                                    color=Colors.TEXT_DARK,
                                    ref=self.__avatar_ref,
                                ),
                                bgcolor=Colors.WHITE,
                            ),
                            Text(
                                self._username,
                                color=Colors.WHITE,
                                ref=self.__username_ref,
                            ),
                            Spacer(),
                            PopupMenuButton(
                                Image(
                                    assets("icons/settings.svg"),
                                    width=24,
                                    height=24,
                                ),
                                items=[
                                    PopupMenuItem(
                                        Text(
                                            "Выгрузить данные",
                                            color=Colors.TEXT_DARK,
                                        ),
                                        mouse_cursor=MouseCursor.CLICK,
                                    ),
                                    PopupMenuItem(
                                        Text(
                                            "Восстановление данных",
                                            color=Colors.TEXT_DARK,
                                        ),
                                        mouse_cursor=MouseCursor.CLICK,
                                    ),
                                ],
                                bgcolor=Colors.WHITE,
                                style=ButtonStyle(mouse_cursor=MouseCursor.CLICK),
                            ),
                        ]
                    ),
                    padding=padding.all(10),
                ),
            ]
        )

    def did_mount(self):
        self.page.run_task(self.__fetch_current_user)

    async def __fetch_current_user(self):
        try:
            user_service = UserService()
            user = await user_service.current()
            self._username = user.username.value
            self.__username_ref.current.value = user.username.value
            self.__avatar_ref.current.value = user.username.value[0]
            self.__username_ref.current.update()
            self.__avatar_ref.current.update()
            FOOTER_CACHE.set("username", user.username.value)
        except Exception as e:
            print(e)
