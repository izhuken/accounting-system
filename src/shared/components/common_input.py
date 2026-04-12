from flet import TextField

from shared.colors import Colors


class CommonInput(TextField):
    def __init__(self, label: str):
        super().__init__(
            label=label,
            color=Colors.TEXT_DARK,
            expand=True,
            expand_loose=True,
        )

    def clean_field(self):
        self.value = None
        self.update()
