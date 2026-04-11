from shared.components.common_page import CommonPage
from shared.lib.router import Router


class WarehouseListPage(CommonPage):
    def __init__(self, router: Router):
        super().__init__("Склады", router)
