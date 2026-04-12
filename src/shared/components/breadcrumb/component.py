from copy import deepcopy

from flet import (
    ButtonStyle,
    Container,
    FilledButton,
    FontWeight,
    Row,
    Text,
    TextDecoration,
    TextStyle,
    margin,
    padding,
)

from shared.colors import Colors
from shared.lib.router import Router

from .config import BreadcrumbsConfig


class Breadcrumbs(Container):
    def __init__(
        self, config: list[BreadcrumbsConfig] = [], router: Router | None = None
    ):
        super().__init__()
        self.config = config
        self.router = router
        self.components = []

        self._build_breadcrumbs()

        self.content = Row(self.components, spacing=5)
        self.margin = margin.only(bottom=-10)

    def _build_breadcrumbs(self):
        for index, section in enumerate(self.config):
            is_last = index == len(self.config) - 1

            text_style = TextStyle(
                color=Colors.BLACK,
                size=12,
                weight=FontWeight.W_600,
                decoration_color=Colors.BLACK,
            )

            if is_last:
                text_style.decoration = TextDecoration.UNDERLINE
                text_style.decoration_thickness = 1
                text_style.decoration_color = Colors.BLACK

            nav_widget = self._create_nav_widget(
                section=section, text_style=text_style, is_last=is_last
            )

            self.components.append(nav_widget)

            if not is_last:
                separator = Text(value="/", color=Colors.BLACK, style=text_style)
                self.components.append(separator)

    def _create_nav_widget(
        self, section: BreadcrumbsConfig, text_style: TextStyle, is_last: bool
    ):
        if is_last or section.link is None:
            return Text(value=section.location, color=Colors.BLACK, style=text_style)

        return Container(
            content=FilledButton(
                content=Text(section.location),
                on_click=lambda _, link=section.link: self.router.go(deepcopy(link)),
                style=ButtonStyle(
                    color=Colors.BLACK,
                    padding=padding.all(0),
                    text_style=text_style,
                    bgcolor=Colors.BACKGROUND,
                    shadow_color=Colors.TRANSPARENT,
                    overlay_color=Colors.TRANSPARENT,
                ),
            ),
            padding=padding.all(0),
            margin=margin.only(top=-10, bottom=-10),
        )
