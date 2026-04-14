from flet import Row

from shared.components.tab_button import TabButton
from shared.lib.router import Router


class MaterialTabs(Row):
    def __init__(self, router: Router) -> None:
        self.router = router

        super().__init__(
            [
                TabButton("Материалы", "/materials", self.router),
                TabButton("Метрики", "/materials/metrics", self.router),
            ]
        )
