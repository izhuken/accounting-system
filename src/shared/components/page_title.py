from flet import Container, FontWeight, Text, margin

from shared.colors import Colors


class PageTitle(Container):
    def __init__(self, title: str):
        super().__init__(
            Text(
                title,
                size=32,
                weight=FontWeight.W_600,
                color=Colors.TEXT_DARK,
            ),
            margin=margin.only(bottom=5),
        )
