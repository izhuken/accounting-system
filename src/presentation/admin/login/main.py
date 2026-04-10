from flet import (
    Container,
    alignment,
)

from core.service.app.user_service import UserService
from shared.lib.router import Router

from .components.login_form import LoginForm


class LoginPage(Container):
    def __init__(self, router: Router):
        self.router = router
        self.auth_service = UserService()
        super().__init__(
            LoginForm(self.router),
            alignment=alignment.Alignment.CENTER,
            expand=True,
        )

    def did_mount(self):
        pass
        # if APP_CONFIG.is_dev_mode:
        # self.router.go("/order")
