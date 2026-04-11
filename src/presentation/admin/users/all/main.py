from shared.components.common_page import CommonPage
from shared.lib.router import Router


class UserListPage(CommonPage):
    def __init__(self, router: Router):
        super().__init__("Пользователи", router)
