from flet import Container


class Spacer(Container):
    def __init__(self):
        super().__init__(expand=True)
