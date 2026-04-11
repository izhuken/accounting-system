from flet import CupertinoButton, Image, MouseCursor, Row, Text, border_radius, padding

from shared.colors import Colors
from shared.lib import Router, assets


def NavButton(title: str, icon: str, route: str, router: Router):
    return CupertinoButton(
        content=Row(
            [
                Image(assets(icon), width=14, height=14),
                Text(title, color=Colors.WHITE),
            ]
        ),
        border_radius=border_radius.all(5),
        bgcolor=Colors.BLUE_ACTIVE_DARK if router.is_current_page(route) else None,
        padding=padding.only(left=14),
        on_click=lambda x: router.go(route),
        mouse_cursor=MouseCursor.CLICK,
    )
