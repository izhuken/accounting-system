from flet import Column, Container, Row, padding

from shared.components.navbar import NavBar
from shared.components.page_title import PageTitle
from shared.lib.router import Router


class CommonPage(Row):
    def __init__(self, title: str, router: Router, content: list[Container] = []):
        self.router = router

        super().__init__(
            [
                NavBar(self.router),
                Container(
                    Column(
                        [PageTitle(title), *content],
                    ),
                    expand=True,
                    padding=padding.only(left=20, right=20, top=20, bottom=20),
                ),
            ],
            spacing=0,
        )
